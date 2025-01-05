from typing import Optional, Dict, Any
from src.client import (
    SpaceTradersClient,
    SpaceTradersError,
    ValidationError,
    ResourceNotFoundError,
    InsufficientResourcesError,
)

class ShipPurchaseError(Exception):
    """Custom exception for ship purchase errors"""
    pass

def find_and_purchase_ship(
    client: SpaceTradersClient,
    ship_type: str,
    system: str
) -> Optional[Dict[str, Any]]:
    """Find a shipyard and purchase the specified ship type"""
    try:
        # Find shipyards in system
        waypoints = client.get_system_waypoints(system)["data"]
        shipyards = [
            wp for wp in waypoints
            if any(trait["symbol"] == "SHIPYARD" for trait in wp.get("traits", []))
        ]
        
        if not shipyards:
            raise ShipPurchaseError(f"No shipyards found in system {system}")
            
        # Try each shipyard until we find one selling our ship
        for shipyard in shipyards:
            try:
                result = client.purchase_ship(ship_type, shipyard["symbol"])
                print(f"Successfully purchased {ship_type} at {shipyard['symbol']}")
                return result["data"]["ship"]
            except ValidationError:
                continue  # Try next shipyard
            except InsufficientResourcesError as e:
                raise ShipPurchaseError(f"Insufficient credits to purchase ship: {str(e)}")
                
        raise ShipPurchaseError(f"Could not find {ship_type} for sale at any shipyard")
        
    except ResourceNotFoundError as e:
        raise ShipPurchaseError(f"System or waypoint not found: {str(e)}")
    except SpaceTradersError as e:
        raise ShipPurchaseError(f"Error during ship purchase process: {str(e)}")

