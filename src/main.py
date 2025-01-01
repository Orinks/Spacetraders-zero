import os
from typing import Optional

from dotenv import load_dotenv

from automation.contract_mining import (ContractMiningError,
                                        handle_contract_mining)
from automation.coordinated_mining import (CoordinatedMiningError,
                                           coordinate_mining)
from automation.mining import MiningError
from client import ApiError, SpaceTradersClient


def initialize_client() -> Optional[SpaceTradersClient]:
    """Initialize the SpaceTraders client"""
    try:
        load_dotenv()
        token = os.getenv("SPACETRADERS_TOKEN")
        if not token:
            print("No token found in .env file")
            return None
        return SpaceTradersClient(token)
    except Exception as e:
        print(f"Failed to initialize client: {str(e)}")
        return None


def display_agent_info(client: SpaceTradersClient) -> None:
    """Display agent information"""
    try:
        agent_info = client.get_agent()
        print("\nAgent Information:")
        print(f"Symbol: {agent_info['data']['symbol']}")
        print(f"Credits: {agent_info['data']['credits']}")
        print(f"Headquarters: {agent_info['data']['headquarters']}")
    except ApiError as e:
        print(f"Failed to get agent info: {str(e)}")


def check_shipyard(client: SpaceTradersClient) -> None:
    """Check shipyard and buy mining ship if needed"""
    try:
        agent_info = client.get_agent()
        headquarters = agent_info["data"]["headquarters"]
        system = "-".join(headquarters.split("-")[:2])

        # Try common shipyard locations
        shipyard_locations = ["H54", "H52", "H51"]
        shipyard = None

        for loc in shipyard_locations:
            try:
                waypoint_symbol = f"{system}-{loc}"
                waypoint = client.get_waypoint(system, waypoint_symbol)
                if any(
                    trait["symbol"] == "SHIPYARD"
                    for trait in waypoint["data"].get("traits", [])
                ):
                    shipyard = waypoint_symbol
                    break
            except ApiError:
                continue

        if not shipyard:
            print("No shipyard found in common locations")
            return

        print(f"\nChecking shipyard at {shipyard}...")

        # List current ships
        ships = client.list_ships()
        mining_ships = [
            ship
            for ship in ships["data"]
            if (
                ship["registration"]["role"] == "EXCAVATOR"
                and any(
                    mount["symbol"].startswith("MOUNT_MINING_LASER")
                    for mount in ship["mounts"]
                )
            )
        ]

        if mining_ships:
            print("\nShipyard status: Already own a mining drone")
            return

        # Get available ships at shipyard
        available_ships = client.get_shipyard(system, shipyard)
        mining_drones = [
            ship
            for ship in available_ships["data"]["ships"]
            if ship["type"] == "SHIP_MINING_DRONE"
        ]

        if not mining_drones:
            print("No mining drones available for purchase")
            return

        drone = mining_drones[0]
        if agent_info["data"]["credits"] < drone["purchasePrice"]:
            print("Not enough credits to buy a mining drone")
            return

        print(f"Purchasing mining drone for {drone['purchasePrice']} credits...")
        purchase_result = client.purchase_ship(drone["type"], shipyard)
        print("Successfully purchased mining drone!")
        print(f"New ship: {purchase_result['data']['ship']['symbol']}")

    except ApiError as e:
        print(f"Failed to check shipyard: {str(e)}")


def display_ships(client: SpaceTradersClient) -> None:
    """Display owned ships"""
    try:
        ships = client.list_ships()
        print("\nOwned Ships:")
        for ship in ships["data"]:
            print(f"Ship Symbol: {ship['symbol']}")
            print(f"Location: {ship['nav']['waypointSymbol']}")
            print(f"Status: {ship['nav']['status']}")
            print("---")
    except ApiError as e:
        print(f"Failed to list ships: {str(e)}")


def display_menu() -> str:
    """Display menu and get user choice"""
    print("\nAvailable Operations:")
    print("1. Contract Mining (Single Ship)")
    print("2. Coordinated Mining (Command Ship + Mining Drone)")
    print("3. Exit")
    return input("Choose an operation (1-3): ")


def find_mining_ships(
    client: SpaceTradersClient,
) -> tuple[Optional[str], Optional[str]]:
    """Find command ship and mining drone from owned ships"""
    try:
        ships = client.list_ships()
        command_ship = None
        mining_drone = None

        for ship in ships["data"]:
            # Get detailed ship info
            ship_detail = client.get_my_ship(ship["symbol"])["data"]
            role = ship_detail["registration"]["role"]

            # Command ships have COMMAND role
            if role == "COMMAND":
                command_ship = ship["symbol"]
            # Mining ships have EXCAVATOR role
            elif role == "EXCAVATOR":
                mining_drone = ship["symbol"]

            if command_ship and mining_drone:
                break

        return command_ship, mining_drone

    except ApiError as e:
        print(f"Failed to find mining ships: {str(e)}")
        return None, None


def main():
    """Main function to run the game loop"""
    try:
        # Initialize client
        client = initialize_client()
        if not client:
            print("Failed to initialize client.")
            return

        # Display agent info
        display_agent_info(client)

        # Check shipyard and buy mining ship if needed
        check_shipyard(client)

        # Display owned ships
        display_ships(client)

        while True:
            choice = display_menu()

            if choice == "1":
                try:
                    handle_contract_mining(client)
                except (ContractMiningError, MiningError) as e:
                    print(f"\nMining operation failed: {str(e)}")

            elif choice == "2":
                try:
                    # Find command ship and mining drone
                    command_ship, mining_drone = find_mining_ships(client)

                    if not command_ship or not mining_drone:
                        print(
                            "\nError: Need both a command ship and mining drone for coordinated mining."
                        )
                        print("Command ship should have COMMAND role.")
                        print("Mining drone should have EXCAVATOR role.")
                        continue

                    print(f"\nStarting coordinated mining with:")
                    print(f"Command Ship: {command_ship}")
                    print(f"Mining Drone: {mining_drone}")

                    # Start coordinated mining operation
                    coordinate_mining(client, command_ship, mining_drone)

                except (CoordinatedMiningError, MiningError) as e:
                    print(f"\nCoordinated mining operation failed: {str(e)}")

            elif choice == "3":
                print("\nExiting program...")
                break

            else:
                print("\nInvalid choice. Please try again.")

    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")


if __name__ == "__main__":
    main()
