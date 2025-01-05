from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
import asyncio
import logging

from src.client import SpaceTradersClient
from src.exceptions import (
    SpaceTradersError,
    ValidationError,
    NetworkError
)
from .coordinated_mining import coordinate_mining, find_mining_ships
from .mining import (
    find_nearest_asteroid_field,
    prepare_for_mining,
    mine_resources,
    sell_all_cargo,
    check_and_refuel,
)
from .models import Ship, ShipCargo

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class MiningTarget:
    waypoint_symbol: str
    resource_type: Optional[str] = None
    units_required: Optional[int] = None
    delivery_destination: Optional[str] = None


class MiningManager:
    def __init__(self, client: SpaceTradersClient):
        self.client = client
        self.command_ship: Optional[Ship] = None
        self.mining_drone: Optional[Ship] = None
        self.is_coordinated = False
    
    def initialize_mining_ships(self) -> bool:
        """Initialize mining ships, preferring coordinated mining if possible."""
        try:
            # Try to find command ship and mining drone for coordinated mining
            command_ship, mining_drones = find_mining_ships(self.client)
            
            if command_ship and mining_drones:
                self.command_ship = command_ship
                self.mining_drone = mining_drones[0] if mining_drones else None
                self.is_coordinated = bool(self.command_ship and self.mining_drone)
                if self.is_coordinated:
                    logger.info(
                        f"Using coordinated mining with command ship {command_ship.symbol} "
                        f"and mining drone {mining_drones[0].symbol}"
                    )
                    return True
                
            # If coordinated mining not available, find any mining ship
            ships = self.client.list_ships()["data"]
            for ship_data in ships:
                ship = Ship.model_validate(ship_data)
                if any(mount.symbol.startswith("MOUNT_MINING_LASER") for mount in ship.mounts):
                    self.mining_drone = ship
                    logger.info(f"Using solo mining with ship {ship.symbol}")
                    return True
                    
            logger.warning("No mining ships found")
            return False
            
        except ValidationError as e:
            logger.error(f"Error validating ships: {str(e)}")
            return False
        except NetworkError as e:
            logger.error(f"Network error while initializing ships: {str(e)}")
            return False
        except SpaceTradersError as e:
            logger.error(f"Unexpected error initializing mining ships: {str(e)}")
            return False
    
    async def mine_resources(
        self,
        target: MiningTarget,
        contract_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Mine resources using either coordinated or solo mining."""
        if not self.mining_drone:
            if not self.initialize_mining_ships():
                return []
        
        try:
            if self.is_coordinated and self.command_ship and self.mining_drone:
                # Use coordinated mining
                market_symbol = target.delivery_destination or self.command_ship.nav.waypoint_symbol
                await coordinate_mining(self.client, market_symbol)
                return []  # Coordinated mining handles its own cargo
            elif self.mining_drone:
                # Use solo mining
                success, asteroid = prepare_for_mining(
                    self.client,
                    self.mining_drone.symbol,
                    target.resource_type
                )
                
                if not success or not asteroid:
                    logger.error("Failed to prepare for mining")
                    return []
                    
                return mine_resources(
                    self.client,
                    self.mining_drone.symbol,
                    target.resource_type,
                    target.units_required
                )
                
            return []
                
        except SpaceTradersError as e:
            if "cooldown" in str(e).lower():
                logger.info("Mining on cooldown")
            else:
                logger.error(f"Mining operation failed: {str(e)}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error during mining operation: {str(e)}")
            return []
    
    def sell_cargo(self, ship_symbol: str) -> List[Dict[str, Any]]:
        """Sell cargo from the specified ship."""
        try:
            return sell_all_cargo(self.client, ship_symbol)
        except SpaceTradersError as e:
            logger.error(f"Failed to sell cargo: {str(e)}")
            return []
    
    def check_fuel(self, ship_symbol: str) -> None:
        """Check and refuel the specified ship if needed."""
        try:
            check_and_refuel(self.client, ship_symbol)
        except SpaceTradersError as e:
            logger.error(f"Failed to check/refuel: {str(e)}")
    
    def get_mining_status(self) -> Dict[str, Any]:
        """Get current status of mining operations."""
        status: Dict[str, Any] = {
            "mode": "coordinated" if self.is_coordinated else "solo",
            "ships": {}
        }
        
        try:
            if self.command_ship:
                command_info = self.client.get_my_ship(self.command_ship.symbol)["data"]
                status["ships"]["command"] = Ship.model_validate(command_info)
                
            if self.mining_drone:
                drone_info = self.client.get_my_ship(self.mining_drone.symbol)["data"]
                status["ships"]["drone"] = Ship.model_validate(drone_info)
                
        except ValidationError as e:
            logger.error(f"Invalid ship status data: {str(e)}")
        except NetworkError as e:
            logger.error(f"Network error getting status: {str(e)}")
        except SpaceTradersError as e:
            logger.error(f"Failed to get mining status: {str(e)}")
            
        return status 