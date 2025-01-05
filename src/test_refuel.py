import os
import time
from typing import Any, Dict, Optional

from src.client import SpaceTradersClient

print("Starting test_refuel.py...")  # Debug print


def find_mining_ship(ships_data: list) -> Optional[Dict[str, Any]]:
    """Find the mining ship from the list of ships"""
    for ship in ships_data:
        if ship["registration"]["role"] == "EXCAVATOR":
            return ship
    return None


def test_refuel():
    print("Initializing client...")  # Debug print
    client = SpaceTradersClient(os.environ["SPACETRADERS_TOKEN"])

    # Get mining ship
    ships = client.list_ships()
    if not ships["data"]:
        print("No ships available")
        return

    mining_ship = find_mining_ship(ships["data"])
    if not mining_ship:
        print("No mining ship found")
        return

    ship_symbol = mining_ship["symbol"]
    print(f"\nTesting refuel with mining ship {ship_symbol}")

    try:
        # Get current nav status
        nav = client.get_ship_nav(ship_symbol)
        system = nav["data"]["systemSymbol"]
        current_waypoint = nav["data"]["waypointSymbol"]
        status = nav["data"]["status"]
        print(f"\nCurrent location: {current_waypoint}")
        print(f"Current status: {status}")

        # Get ship details for fuel
        ship_info = client.get_my_ship(ship_symbol)
        fuel = ship_info["data"]["fuel"]
        print(f"\nFuel status: {fuel['current']}/{fuel['capacity']} units")

        # Get current coordinates
        waypoint_info = client.get_waypoint(system, current_waypoint)
        current_x = waypoint_info["data"]["x"]
        current_y = waypoint_info["data"]["y"]

        # Find nearest fuel station
        print("\nLooking for fuel stations...")
        stations = client.find_fuel_stations_in_system(system)
        if not stations:
            print("No fuel stations found!")
            return

        # Calculate closest station
        def distance(waypoint):
            dx = waypoint["x"] - current_x
            dy = waypoint["y"] - current_y
            return (dx * dx + dy * dy) ** 0.5

        nearest = min(stations, key=distance)
        print(
            f"\nNearest fuel station: {nearest['symbol']} at ({nearest['x']}, {nearest['y']})"
        )

        # Navigate to station if not already there
        if current_waypoint != nearest["symbol"]:
            print(f"\nNavigating to {nearest['symbol']}...")

            # Make sure we're in orbit
            if status != "IN_ORBIT":
                print("Entering orbit...")
                client.orbit_ship(ship_symbol)
                time.sleep(2)  # Wait a moment for orbit
                status = "IN_ORBIT"

            # Navigate
            try:
                print(f"Current status before navigation: {status}")
                print(f"Navigating from {current_waypoint} to {nearest['symbol']}")
                nav_result = client.navigate_ship(ship_symbol, nearest["symbol"])
                arrival = nav_result["data"]["nav"]["route"]["arrival"]
                print(f"Navigation started. Arrival at: {arrival}")

                # Wait for arrival
                print("Waiting for arrival...")
                while True:
                    nav_status = client.get_ship_nav(ship_symbol)
                    current_status = nav_status["data"]["status"]
                    current_waypoint = nav_status["data"]["waypointSymbol"]
                    print(f"Current status: {current_status} at {current_waypoint}")

                    if (
                        current_status == "IN_ORBIT"
                        and current_waypoint == nearest["symbol"]
                    ):
                        break
                    time.sleep(2)

                print("Arrived at fuel station")

            except Exception as e:
                print(f"Navigation failed: {str(e)}")
                print("Navigation error details:")
                print(f"- Ship status: {status}")
                print(f"- Current waypoint: {current_waypoint}")
                print(f"- Target waypoint: {nearest['symbol']}")
                return

        # Dock at station
        try:
            if status != "DOCKED":
                print("\nDocking at station...")
                client.dock_ship(ship_symbol)
                time.sleep(1)
        except Exception as e:
            print(f"Docking failed: {str(e)}")
            return

        # Attempt refuel
        try:
            print("\nAttempting to refuel...")
            result = client.refuel_ship(ship_symbol)
            print(f"Refuel successful!")
            print(f"Units: {result['data']['transaction']['units']}")
            print(f"Cost: {result['data']['transaction']['totalPrice']}")
        except Exception as e:
            print(f"Refuel failed: {str(e)}")

    except Exception as e:
        print(f"Error during test: {str(e)}")


if __name__ == "__main__":
    test_refuel()
