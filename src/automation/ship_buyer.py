from typing import Any, Dict, Optional, Tuple

from client import ApiError, SpaceTradersClient


class ShipPurchaseError(Exception):
    """Custom exception for ship purchase errors"""

    pass


def check_and_buy_mining_drone(
    client: SpaceTradersClient, system_symbol: str, waypoint_symbol: str
) -> Tuple[bool, Optional[Dict[str, Any]], str]:
    """
    Check if a mining drone is available at the shipyard and attempt to purchase it

    Returns:
        Tuple containing:
        - Success status (bool)
        - Purchase response data if successful (Dict or None)
        - Status message (str)
    """
    try:
        # Check if waypoint has a shipyard
        waypoint_data = client.get_waypoint(system_symbol, waypoint_symbol)
        has_shipyard = any(
            trait["symbol"] == "SHIPYARD" for trait in waypoint_data["data"]["traits"]
        )

        if not has_shipyard:
            return False, None, f"No shipyard at waypoint {waypoint_symbol}"

        # Get shipyard data
        shipyard_data = client.get_shipyard(system_symbol, waypoint_symbol)
        ships_for_sale = shipyard_data["data"]["ships"]

        # Check if mining drone is available
        mining_drone = next(
            (ship for ship in ships_for_sale if ship["type"] == "SHIP_MINING_DRONE"),
            None,
        )

        if not mining_drone:
            return False, None, "No mining drones available at this shipyard"

        # Check if we already have a mining drone
        current_ships = client.list_ships()
        if client.has_ship_type(current_ships["data"], "FRAME_DRONE"):
            return False, None, "Already own a mining drone"

        # Check if we have enough credits
        agent_data = client.get_agent_details()
        credits = agent_data["data"]["credits"]
        ship_price = mining_drone["purchasePrice"]

        if credits < ship_price:
            return (
                False,
                None,
                f"Insufficient credits. Need {ship_price}, have {credits}",
            )

        # Purchase the mining drone
        purchase_response = client.purchase_ship("SHIP_MINING_DRONE", waypoint_symbol)

        return True, purchase_response, "Successfully purchased mining drone"

    except ApiError as e:
        raise ShipPurchaseError(f"Error during ship purchase process: {str(e)}")
    except Exception as e:
        raise ShipPurchaseError(f"Unexpected error: {str(e)}")
