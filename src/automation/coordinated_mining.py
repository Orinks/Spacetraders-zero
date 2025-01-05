import time
import logging
from typing import List, Optional, Tuple, Dict, Any
from dataclasses import dataclass
from functools import wraps
import asyncio
from concurrent.futures import ThreadPoolExecutor

from src.client import SpaceTradersClient
from src.exceptions import SpaceTradersError, ValidationError, NetworkError
from .models import Ship, ShipCargo, MiningResult
from .mining import find_nearest_asteroid_field, check_and_refuel


class CoordinatedMiningError(Exception):
    """Custom exception for coordinated mining operation errors"""
    pass


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
CARGO_TRANSFER_THRESHOLD = 0.8  # Transfer at 80% capacity
COMMAND_SHIP_SELL_THRESHOLD = 0.8  # Sell at 80% capacity
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


def retry_on_network_error(max_retries: int = MAX_RETRIES, delay: int = RETRY_DELAY):
    """Decorator to retry operations on network errors"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    if attempt == max_retries - 1:
                        raise
                    logger.warning(f"Network error: {str(e)}. Retrying in {delay}s...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator


@retry_on_network_error()
def find_mining_ships(client: SpaceTradersClient) -> Tuple[Optional[Ship], List[Ship]]:
    """Find command ship and mining drones with improved validation"""
    try:
        ships_data = client.list_ships()["data"]
        command_ship = None
        mining_drones = []
        
        for ship_data in ships_data:
            ship = Ship.model_validate(ship_data)
            if ship.registration["role"] == "COMMAND":
                command_ship = ship
            elif ship.registration["role"] == "EXCAVATOR":
                mining_drones.append(ship)
                
        return command_ship, mining_drones
        
    except ValidationError as e:
        logger.error(f"Failed to validate ship data: {str(e)}")
        raise
    except SpaceTradersError as e:
        logger.error(f"Failed to find mining ships: {str(e)}")
        raise


async def extract_resources(client: SpaceTradersClient, drone: Ship) -> Optional[MiningResult]:
    """Extract resources with a single drone"""
    try:
        result = client._make_request("POST", f"my/ships/{drone.symbol}/extract")
        return MiningResult.model_validate(result["data"])
    except SpaceTradersError as e:
        if "cooldown" in str(e).lower():
            logger.info(f"Mining drone {drone.symbol} cooling down")
        else:
            logger.error(f"Mining error with drone {drone.symbol}: {str(e)}")
    return None


async def transfer_cargo(
    client: SpaceTradersClient,
    drone: Ship,
    command_ship: Ship
) -> bool:
    """Transfer cargo from drone to command ship"""
    try:
        cargo = ShipCargo.model_validate(
            client.get_ship_cargo(drone.symbol)["data"]
        )
        
        for item in cargo.inventory:
            result = client._make_request(
                "POST",
                f"my/ships/{drone.symbol}/transfer",
                data={
                    "tradeSymbol": item["symbol"],
                    "units": item["units"],
                    "shipSymbol": command_ship.symbol
                }
            )
            logger.info(
                f"Transferred {item['units']} units of {item['symbol']} "
                f"from {drone.symbol} to {command_ship.symbol}"
            )
        return True
        
    except SpaceTradersError as e:
        logger.error(f"Failed to transfer cargo: {str(e)}")
        return False


async def navigate_and_sell(
    client: SpaceTradersClient,
    ship: Ship,
    market_symbol: str
) -> bool:
    """Navigate to market and sell cargo"""
    try:
        if ship.nav.waypoint_symbol != market_symbol:
            client.navigate_ship(ship.symbol, market_symbol)
            logger.info(f"Navigating {ship.symbol} to market {market_symbol}")
            # Wait for navigation
            while True:
                nav = client.get_ship_nav(ship.symbol)["data"]
                if nav["status"] == "DOCKED":
                    break
                await asyncio.sleep(1)
                
        cargo = ShipCargo.model_validate(
            client.get_ship_cargo(ship.symbol)["data"]
        )
        
        for item in cargo.inventory:
            result = client.sell_cargo(
                ship_symbol=ship.symbol,
                symbol=item["symbol"],
                units=item["units"]
            )
            logger.info(
                f"Sold {item['units']} units of {item['symbol']} "
                f"from {ship.symbol}"
            )
        return True
        
    except SpaceTradersError as e:
        logger.error(f"Failed to sell cargo: {str(e)}")
        return False


async def monitor_ship_status(
    client: SpaceTradersClient,
    ship: Ship
) -> Ship:
    """Monitor and maintain ship status"""
    try:
        # Check fuel
        check_and_refuel(client, ship.symbol)
        
        # Update ship data
        ship_data = client.get_my_ship(ship.symbol)["data"]
        return Ship.model_validate(ship_data)
        
    except SpaceTradersError as e:
        logger.error(f"Failed to monitor ship status: {str(e)}")
        return ship


async def coordinate_mining(
    client: SpaceTradersClient,
    market_symbol: str
) -> None:
    """Coordinate mining operations between command ship and mining drones"""
    try:
        command_ship, mining_drones = find_mining_ships(client)
        if not command_ship or not mining_drones:
            raise ValueError("Missing required ships for coordinated mining")
            
        system = command_ship.nav.system_symbol
        asteroid_field = find_nearest_asteroid_field(client, system)
        if not asteroid_field:
            raise ValueError("No asteroid field found")
            
        if not market_symbol:
            # Use command ship's current location as market
            market_symbol = command_ship.nav.waypoint_symbol
            
        logger.info(f"Starting coordinated mining operation in system {system}")
        logger.info(f"Using market at {market_symbol}")
        
        while True:
            # Update ship statuses
            tasks = []
            for drone in mining_drones:
                tasks.append(monitor_ship_status(client, drone))
            tasks.append(monitor_ship_status(client, command_ship))
            
            updated_ships = await asyncio.gather(*tasks)
            mining_drones = updated_ships[:-1]
            command_ship = updated_ships[-1]
            
            # Mining phase
            mining_tasks = []
            for drone in mining_drones:
                if drone.cargo.units >= drone.cargo.capacity * CARGO_TRANSFER_THRESHOLD:
                    # Transfer cargo if drone is sufficiently full
                    await transfer_cargo(client, drone, command_ship)
                else:
                    # Mine with drone
                    mining_tasks.append(extract_resources(client, drone))
                    
            if mining_tasks:
                await asyncio.gather(*mining_tasks)
                
            # Check command ship cargo
            if command_ship.cargo.units >= command_ship.cargo.capacity * COMMAND_SHIP_SELL_THRESHOLD:
                await navigate_and_sell(client, command_ship, market_symbol)
                
            await asyncio.sleep(5)  # Brief pause between cycles
            
    except Exception as e:
        logger.error(f"Mining operation failed: {str(e)}")
        raise
