from typing import Optional, Dict, Any, List
from src.client import (
    SpaceTradersClient,
    SpaceTradersError,
    ValidationError,
    ResourceNotFoundError,
    InsufficientResourcesError,
)


def check_shipyard(client: SpaceTradersClient, system: str, waypoint: str) -> Optional[Dict[str, Any]]:
    """Check shipyard at the specified location"""
    try:
        return client.get_shipyard(system, waypoint)
    except (ValidationError, ResourceNotFoundError) as e:
        print(f"Failed to check shipyard: {str(e)}")
    except SpaceTradersError as e:
        print(f"Unexpected error checking shipyard: {str(e)}")
    return None


def find_nearest_shipyard(client: SpaceTradersClient, current_system: str) -> Optional[Dict]:
    """Find the nearest shipyard in the current system"""
    try:
        waypoints = client.list_waypoints(current_system)
        shipyards = [
            wp for wp in waypoints["data"]
            if any(trait["symbol"] == "SHIPYARD" for trait in wp.get("traits", []))
        ]
        
        if not shipyards:
            print("No shipyards found in system")
            return None
            
        return shipyards[0]
    except SpaceTradersError as e:
        print(f"Failed to find shipyard: {str(e)}")
        return None


def purchase_ship(
    client: SpaceTradersClient,
    ship_type: str,
    system: str,
    waypoint: str
) -> Optional[Dict[str, Any]]:
    """
    Purchase a ship of the specified type at the given shipyard
    
    Args:
        client: SpaceTraders client
        ship_type: Type of ship to purchase (e.g., 'SHIP_MINING_DRONE', 'SHIP_SURVEYOR')
        system: System symbol where the shipyard is located
        waypoint: Waypoint symbol of the shipyard
        
    Returns:
        Ship data if purchase successful, None otherwise
    """
    try:
        # Check if shipyard exists and has the ship type
        shipyard = check_shipyard(client, system, waypoint)
        if not shipyard:
            print(f"No shipyard found at {waypoint}")
            return None
            
        ships = shipyard["data"]["ships"]
        ship_types = [ship["type"] for ship in ships]
        
        if ship_type not in ship_types:
            print(f"Ship type {ship_type} not available at this shipyard")
            print("Available ships:", ", ".join(ship_types))
            return None
            
        # Purchase the ship
        result = client.purchase_ship(ship_type, waypoint)
        ship = result["data"]["ship"]
        transaction = result["data"]["transaction"]
        
        print(f"Successfully purchased {ship_type}")
        print(f"Ship symbol: {ship['symbol']}")
        print(f"Price: {transaction['totalPrice']} credits")
        
        return ship
        
    except InsufficientResourcesError:
        print("Insufficient credits to purchase ship")
    except SpaceTradersError as e:
        print(f"Failed to purchase ship: {str(e)}")
    return None


def purchase_mining_drone(
    client: SpaceTradersClient, system: str, waypoint: str
) -> Optional[Dict[str, Any]]:
    """Purchase a mining drone at the specified shipyard"""
    return purchase_ship(client, "SHIP_MINING_DRONE", system, waypoint)


def get_ship_details(client: SpaceTradersClient, ship_symbol: str) -> Optional[Dict[str, Any]]:
    """Get detailed information about a ship"""
    try:
        return client.get_my_ship(ship_symbol)
    except SpaceTradersError as e:
        print(f"Failed to get ship details: {str(e)}")
        return None


def list_all_ships(client: SpaceTradersClient) -> List[Dict[str, Any]]:
    """Get a list of all owned ships"""
    try:
        response = client.list_ships()
        return response["data"]
    except SpaceTradersError as e:
        print(f"Failed to list ships: {str(e)}")
        return []
