import time
from typing import Any, Dict, List, Optional, Tuple

from client import ApiError, SpaceTradersClient


class MiningError(Exception):
    """Custom exception for mining operations"""

    pass


def wait_for_cooldown(client: SpaceTradersClient, ship_symbol: str) -> None:
    """Wait for ship's cooldown to complete"""
    try:
        cooldown = client.get_ship_cooldown(ship_symbol)
        if "data" in cooldown and cooldown["data"].get("remainingSeconds", 0) > 0:
            remaining = cooldown["data"]["remainingSeconds"]
            print(f"Cooling down... {remaining} seconds remaining")
            time.sleep(remaining + 1)  # Add 1 second buffer
    except ApiError:
        # If we can't get cooldown, assume no cooldown
        pass


def find_nearest_asteroid_field(
    client: SpaceTradersClient, ship_symbol: str, resource_type: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    Find the nearest asteroid field to the ship's current location,
    prioritizing asteroids with metal deposits
    """
    try:
        # Get ship's current location
        nav = client.get_ship_nav(ship_symbol)
        current_system = nav["data"]["systemSymbol"]
        current_waypoint = nav["data"]["waypointSymbol"]

        print(f"Current system: {current_system}")
        print(f"Current location: {current_waypoint}")

        # Get all waypoints in the system with pagination
        print("\nSearching for asteroid fields...")
        all_waypoints = []
        page = 1
        while True:
            response = client._make_request(
                "GET", f"systems/{current_system}/waypoints?page={page}"
            )
            all_waypoints.extend(response["data"])
            if page * 10 >= response["meta"]["total"]:
                break
            page += 1

        print(f"Found {len(all_waypoints)} waypoints in system")

        # First, look for engineered asteroids with metal deposits
        print("\nLooking for engineered asteroids with metal deposits...")
        engineered_asteroids = [
            wp
            for wp in all_waypoints
            if wp["type"] == "ENGINEERED_ASTEROID"
            and any(
                trait["symbol"] == "COMMON_METAL_DEPOSITS"
                for trait in wp.get("traits", [])
            )
        ]

        if engineered_asteroids:
            target = engineered_asteroids[0]
            print(f"Found engineered asteroid: {target['symbol']}")
            print("Asteroid traits:")
            for trait in target["traits"]:
                print(f"- {trait['name']}: {trait['description']}")
            return target

        # Next, look for regular asteroids with metal deposits
        print("\nLooking for regular asteroids with metal deposits...")
        metal_asteroids = [
            wp
            for wp in all_waypoints
            if wp["type"] == "ASTEROID"
            and any(
                trait["symbol"] == "COMMON_METAL_DEPOSITS"
                for trait in wp.get("traits", [])
            )
        ]

        if metal_asteroids:
            # Find the closest one to current location
            current_x = next(
                wp["x"] for wp in all_waypoints if wp["symbol"] == current_waypoint
            )
            current_y = next(
                wp["y"] for wp in all_waypoints if wp["symbol"] == current_waypoint
            )

            # Sort by distance
            metal_asteroids.sort(
                key=lambda wp: ((wp["x"] - current_x) ** 2 + (wp["y"] - current_y) ** 2)
                ** 0.5
            )

            target = metal_asteroids[0]
            print(f"Found metal-rich asteroid: {target['symbol']}")
            print("Asteroid traits:")
            for trait in target["traits"]:
                print(f"- {trait['name']}: {trait['description']}")
            print(
                f"Distance: {int(((target['x'] - current_x) ** 2 + (target['y'] - current_y) ** 2) ** 0.5)} units"
            )
            return target

        # If no metal deposits, look for any asteroid field
        print("\nLooking for any asteroid fields...")
        asteroid_fields = [wp for wp in all_waypoints if wp["type"] == "ASTEROID"]

        if asteroid_fields:
            # Find the closest one
            current_x = next(
                wp["x"] for wp in all_waypoints if wp["symbol"] == current_waypoint
            )
            current_y = next(
                wp["y"] for wp in all_waypoints if wp["symbol"] == current_waypoint
            )

            # Sort by distance
            asteroid_fields.sort(
                key=lambda wp: ((wp["x"] - current_x) ** 2 + (wp["y"] - current_y) ** 2)
                ** 0.5
            )

            target = asteroid_fields[0]
            print(f"Found asteroid: {target['symbol']}")
            print("Asteroid traits:")
            for trait in target.get("traits", []):
                print(f"- {trait['name']}: {trait['description']}")
            print(
                f"Distance: {int(((target['x'] - current_x) ** 2 + (target['y'] - current_y) ** 2) ** 0.5)} units"
            )
            return target

        print("Could not find any suitable asteroid fields")
        return None

    except ApiError as e:
        print(f"Error finding asteroid field: {str(e)}")
        raise MiningError(f"Failed to find asteroid field: {str(e)}")
    except Exception as e:
        print(f"Unexpected error finding asteroid field: {str(e)}")
        raise MiningError(f"Failed to find asteroid field: {str(e)}")


def calculate_transit_time(nav_data: Dict[str, Any]) -> str:
    """Calculate and format transit time from navigation data"""
    from datetime import datetime

    departure = datetime.fromisoformat(
        nav_data["route"]["departureTime"].replace("Z", "+00:00")
    )
    arrival = datetime.fromisoformat(
        nav_data["route"]["arrival"].replace("Z", "+00:00")
    )
    duration = arrival - departure

    minutes = duration.total_seconds() / 60
    return f"{int(minutes)} minutes"


def calculate_remaining_time(arrival_time: str) -> str:
    """Calculate and format remaining time until arrival"""
    from datetime import datetime

    arrival = datetime.fromisoformat(arrival_time.replace("Z", "+00:00"))
    now = datetime.now(arrival.tzinfo)
    remaining = arrival - now

    minutes = int(remaining.total_seconds() / 60)
    seconds = int(remaining.total_seconds() % 60)

    if minutes > 0:
        return f"{minutes}m {seconds}s remaining"
    return f"{seconds}s remaining"


def wait_for_arrival(
    client: SpaceTradersClient, ship_symbol: str, nav_data: Dict[str, Any]
) -> None:
    """Wait for ship to arrive at destination with time updates every 30 seconds"""
    arrival_time = nav_data["route"]["arrival"]
    update_interval = 30  # seconds between updates
    last_update = time.time()  # Initialize with current time

    while nav_data["status"] == "IN_TRANSIT":
        current_time = time.time()

        # Only update if enough time has passed since last update
        if current_time - last_update >= update_interval:
            remaining = calculate_remaining_time(arrival_time)
            print(f"In transit... {remaining}")
            last_update = current_time

        time.sleep(5)  # Still check status every 5 seconds
        nav = client.get_ship_nav(ship_symbol)
        nav_data = nav["data"]


def check_and_refuel(client: SpaceTradersClient, ship_symbol: str) -> None:
    """Check fuel levels and refuel if needed or if at a fuel station"""
    try:
        # Get ship details for fuel
        ship_info = client.get_my_ship(ship_symbol)
        fuel = ship_info["data"]["fuel"]
        print(f"\nFuel status: {fuel['current']}/{fuel['capacity']} units")

        # Get current nav status
        nav = client.get_ship_nav(ship_symbol)
        system = nav["data"]["systemSymbol"]
        current_waypoint = nav["data"]["waypointSymbol"]
        status = nav["data"]["status"]

        # Check if current waypoint sells fuel
        if client.check_waypoint_sells_fuel(system, current_waypoint):
            # If we're at a fuel station and not at full fuel, top up
            if fuel["current"] < fuel["capacity"]:
                print("At fuel station. Topping up fuel...")
                if status != "DOCKED":
                    client.dock_ship(ship_symbol)
                client.refuel_ship(ship_symbol)
                # After refueling, enter orbit for mining
                print("Entering orbit after refueling...")
                client.orbit_ship(ship_symbol)
            return

        # If not at a fuel station, only search for one if fuel is low
        if fuel["current"] / fuel["capacity"] >= 0.3:
            return

        print("Fuel low. Attempting to refuel...")
        print(f"\nCurrent status: {status} at {current_waypoint}")

        # Get current coordinates
        waypoint_info = client.get_waypoint(system, current_waypoint)
        current_x = waypoint_info["data"]["x"]
        current_y = waypoint_info["data"]["y"]
        print(f"Current coordinates: ({current_x}, {current_y})")

        # Find nearest fuel station
        print("\nLooking for nearest fuel station...")
        stations = client.find_fuel_stations_in_system(system)
        if not stations:
            raise Exception("No fuel stations found in system!")

        # Calculate closest station
        def distance(waypoint):
            dx = waypoint["x"] - current_x
            dy = waypoint["y"] - current_y
            return (dx * dx + dy * dy) ** 0.5

        nearest = min(stations, key=distance)
        print(
            f"Found fuel station at {nearest['symbol']} ({nearest['x']}, {nearest['y']})"
        )
        print(f"Distance: {int(distance(nearest))} units")

        # Navigate to station if needed
        if current_waypoint != nearest["symbol"]:
            if status != "IN_ORBIT":
                print("Entering orbit...")
                client.orbit_ship(ship_symbol)
                time.sleep(2)  # Wait a moment for orbit
                # Get updated status
                nav = client.get_ship_nav(ship_symbol)
                status = nav["data"]["status"]

            print(f"\nPreparing navigation:")
            print(f"- Ship status: {status}")
            print(f"- From: {current_waypoint} ({current_x}, {current_y})")
            print(f"- To: {nearest['symbol']} ({nearest['x']}, {nearest['y']})")

            try:
                nav_result = client.navigate_ship(ship_symbol, nearest["symbol"])
                nav_data = nav_result["data"]["nav"]
                arrival = nav_data["route"]["arrival"]
                print(f"Navigation started. Arrival at: {arrival}")

                # Wait for arrival with progress updates
                print("\nWaiting for arrival...")
                while True:
                    nav_status = client.get_ship_nav(ship_symbol)
                    current_status = nav_status["data"]["status"]
                    current_loc = nav_status["data"]["waypointSymbol"]
                    print(f"Status: {current_status} at {current_loc}")

                    if (
                        current_status == "IN_ORBIT"
                        and current_loc == nearest["symbol"]
                    ):
                        break
                    time.sleep(2)

                print("Arrived at fuel station")

            except Exception as e:
                print(f"\nNavigation failed: {str(e)}")
                print("Error details:")
                print(f"- Ship status: {status}")
                print(f"- Current waypoint: {current_waypoint}")
                print(f"- Target waypoint: {nearest['symbol']}")
                raise

        # Dock and refuel
        if status != "DOCKED":
            print("Docking at fuel station...")
            client.dock_ship(ship_symbol)
            time.sleep(1)

        print("Refueling...")
        result = client.refuel_ship(ship_symbol)
        print(f"Refueled {result['data']['transaction']['units']} units")
        print(f"Cost: {result['data']['transaction']['totalPrice']} credits")

    except Exception as e:
        raise Exception(f"Failed to check/refuel: {str(e)}")


def find_command_ship(client: SpaceTradersClient) -> Optional[Dict[str, Any]]:
    """Find the command ship"""
    try:
        ships = client.list_ships()
        # First try to find a dedicated command ship
        command_ship = next(
            (
                ship
                for ship in ships["data"]
                if ship["registration"]["role"] == "COMMAND"
            ),
            None,
        )
        if command_ship:
            print(f"Found command ship: {command_ship['symbol']}")
            return command_ship

        # If no dedicated command ship, look for any non-mining ship
        command_ship = next(
            (
                ship
                for ship in ships["data"]
                if not any(
                    mount["symbol"].startswith("MOUNT_MINING_LASER")
                    for mount in ship["mounts"]
                )
            ),
            None,
        )
        if command_ship:
            print(f"Using {command_ship['symbol']} as command ship")
            return command_ship

        return None
    except ApiError as e:
        print(f"Error finding command ship: {str(e)}")
        return None


def find_mining_drone(client: SpaceTradersClient) -> Optional[Dict[str, Any]]:
    """Find the mining drone"""
    try:
        ships = client.list_ships()
        # First try to find a dedicated mining drone
        mining_drone = next(
            (
                ship
                for ship in ships["data"]
                if ship["registration"]["role"] == "EXCAVATOR"
                and any(
                    mount["symbol"].startswith("MOUNT_MINING_LASER")
                    for mount in ship["mounts"]
                )
            ),
            None,
        )
        if mining_drone:
            print(f"Found mining drone: {mining_drone['symbol']}")
            return mining_drone

        # If no dedicated mining drone, look for any ship with mining lasers
        mining_drone = next(
            (
                ship
                for ship in ships["data"]
                if any(
                    mount["symbol"].startswith("MOUNT_MINING_LASER")
                    for mount in ship["mounts"]
                )
            ),
            None,
        )
        if mining_drone:
            print(f"Using {mining_drone['symbol']} as mining drone")
            return mining_drone

        return None
    except ApiError as e:
        print(f"Error finding mining drone: {str(e)}")
        return None


def prepare_for_mining(
    client: SpaceTradersClient, ship_symbol: str, resource_type: Optional[str] = None
) -> Tuple[bool, Optional[Dict[str, Any]]]:
    """
    Prepare ship for mining by finding an asteroid field and navigating to it.
    If the ship is a command ship, it will command the mining drone to the location.
    """
    try:
        print("\nPreparing for mining operations...")

        # Get ship details
        ship_info = client.get_my_ship(ship_symbol)
        is_command_ship = ship_info["data"]["registration"][
            "role"
        ] == "COMMAND" and not any(
            mount["symbol"].startswith("MOUNT_MINING_LASER")
            for mount in ship_info["data"]["mounts"]
        )

        # If this is a command ship, find and use the mining drone
        if is_command_ship:
            print("Command ship detected. Finding mining drone...")
            mining_drone = find_mining_drone(client)
            if not mining_drone:
                print("No mining drone found.")
                return False, None
            ship_symbol = mining_drone["symbol"]
            print(f"Using mining drone: {ship_symbol}")

        # Get ship's current location
        nav = client.get_ship_nav(ship_symbol)
        current_system = nav["data"]["systemSymbol"]
        current_status = nav["data"]["status"]
        current_waypoint = nav["data"]["waypointSymbol"]
        print(f"Ship is in system {current_system}")
        print(f"Current location: {current_waypoint}")
        print(f"Current status: {current_status}")

        # Get ship details for fuel
        ship_info = client.get_my_ship(ship_symbol)
        fuel = ship_info["data"]["fuel"]
        print(f"\nFuel status: {fuel['current']}/{fuel['capacity']} units")

        # Find nearest asteroid field
        asteroid_field = find_nearest_asteroid_field(client, ship_symbol, resource_type)
        if not asteroid_field:
            print("No suitable asteroid fields found.")
            return False, None

        target_waypoint = asteroid_field["symbol"]
        print(f"\nFound target asteroid field: {target_waypoint}")

        # Always ensure we're in orbit before attempting navigation
        if current_status == "DOCKED":
            print("Entering orbit before navigation...")
            client.orbit_ship(ship_symbol)
            nav = client.get_ship_nav(ship_symbol)
            current_status = nav["data"]["status"]
            print(f"New status: {current_status}")

        # If we're already at the target, just ensure proper orbit
        if current_waypoint == target_waypoint:
            print("Already at target asteroid.")
            if current_status != "IN_ORBIT":
                print("Entering orbit for mining...")
                client.orbit_ship(ship_symbol)
            return True, asteroid_field

        print(f"\nPlanning navigation to {target_waypoint}...")
        try:
            nav_result = client.navigate_ship(ship_symbol, target_waypoint)
            nav_data = nav_result["data"]["nav"]
            transit_time = calculate_transit_time(nav_data)
            print(f"Navigation started. Total transit time: {transit_time}")

            # Wait for arrival with time updates
            wait_for_arrival(client, ship_symbol, nav_data)
            print("Arrived at asteroid field.")
            return True, asteroid_field

        except ApiError as e:
            print(f"Navigation error: {str(e)}")
            print("Navigation error details:")
            print(f"- Ship status: {current_status}")
            print(f"- Current waypoint: {current_waypoint}")
            print(f"- Target waypoint: {target_waypoint}")
            raise

    except ApiError as e:
        print(f"API Error during mining preparation: {str(e)}")
        raise MiningError(f"Failed to prepare for mining: {str(e)}")
    except Exception as e:
        print(f"Unexpected error during mining preparation: {str(e)}")
        raise MiningError(f"Failed to prepare for mining: {str(e)}")


def mine_resources(
    client: SpaceTradersClient,
    ship_symbol: str,
    resource_type: Optional[str] = None,
    max_cargo: Optional[int] = None,
) -> List[Dict[str, Any]]:
    """
    Mine resources until cargo is full or max_cargo is reached

    Args:
        client: SpaceTraders client
        ship_symbol: Symbol of the mining ship
        resource_type: Optional specific resource to mine
        max_cargo: Maximum number of cargo units to mine (None for unlimited)

    Returns:
        List of mining results
    """
    results = []

    try:
        # Prepare for mining
        success, asteroid_field = prepare_for_mining(client, ship_symbol, resource_type)
        if not success or not asteroid_field:
            raise MiningError("Failed to find suitable mining location")

        asteroid_symbol = asteroid_field.get("symbol", "UNKNOWN")
        print(f"\nBeginning mining operations at {asteroid_symbol}")
        if resource_type:
            print(f"Targeting resource: {resource_type}")

        # Check if current location sells fuel and top up if needed
        nav = client.get_ship_nav(ship_symbol)
        system = nav["data"]["systemSymbol"]
        current_waypoint = nav["data"]["waypointSymbol"]

        if client.check_waypoint_sells_fuel(system, current_waypoint):
            ship_info = client.get_my_ship(ship_symbol)
            fuel = ship_info["data"]["fuel"]
            if fuel["current"] < fuel["capacity"]:
                print("\nCurrent location sells fuel. Taking opportunity to top up...")
                if nav["data"]["status"] != "DOCKED":
                    client.dock_ship(ship_symbol)
                client.refuel_ship(ship_symbol)
                print("Entering orbit for mining...")
                client.orbit_ship(ship_symbol)

        while True:
            # Check cargo space
            cargo = client.get_ship_cargo(ship_symbol)
            current_units = sum(item["units"] for item in cargo["data"]["inventory"])
            capacity = cargo["data"]["capacity"]

            print(f"\nCargo status: {current_units}/{capacity} units")

            if current_units >= capacity:
                print(f"Cargo full ({current_units}/{capacity} units)")
                break

            if max_cargo and current_units >= max_cargo:
                print(f"Reached max cargo limit ({current_units}/{max_cargo} units)")
                break

            # Check and refuel if needed (only if fuel is low)
            check_and_refuel(client, ship_symbol)

            # Ensure we're in orbit before mining
            nav = client.get_ship_nav(ship_symbol)
            if nav["data"]["status"] != "IN_ORBIT":
                print("Entering orbit for mining...")
                client.orbit_ship(ship_symbol)

            # Wait for any cooldown
            wait_for_cooldown(client, ship_symbol)

            # Extract resources
            try:
                print("\nExtracting resources...")
                result = client.extract_resources(ship_symbol)
                extraction = result["data"]["extraction"]
                cargo_item = extraction["yield"]

                print(
                    f"Successfully extracted {cargo_item['units']} units of {cargo_item['symbol']}"
                )

                # Only add to results if we got what we wanted
                if not resource_type or cargo_item["symbol"] == resource_type:
                    results.append(result)

            except ApiError as e:
                if "cooldown" in str(e).lower():
                    wait_for_cooldown(client, ship_symbol)
                else:
                    print(f"Extraction failed: {str(e)}")
                    raise

    except ApiError as e:
        print(f"API Error during mining: {str(e)}")
        raise MiningError(f"Mining operation failed: {str(e)}")
    except Exception as e:
        print(f"Unexpected error during mining: {str(e)}")
        raise MiningError(f"Mining operation failed: {str(e)}")

    return results


def sell_all_cargo(
    client: SpaceTradersClient, ship_symbol: str
) -> List[Dict[str, Any]]:
    """
    Sell all cargo on the ship

    Returns:
        List of sale transactions
    """
    results = []

    try:
        # Get cargo
        cargo = client.get_ship_cargo(ship_symbol)

        # Sell each item
        for item in cargo["data"]["inventory"]:
            try:
                result = client.sell_cargo(ship_symbol, item["symbol"], item["units"])
                transaction = result["data"]["transaction"]
                print(
                    f"Sold {transaction['units']} units of {transaction['tradeSymbol']} "
                    f"for {transaction['totalPrice']} credits"
                )
                results.append(result)

            except ApiError as e:
                print(f"Failed to sell {item['symbol']}: {str(e)}")

    except ApiError as e:
        raise MiningError(f"Failed to sell cargo: {str(e)}")
    except Exception as e:
        raise MiningError(f"Unexpected error while selling: {str(e)}")

    return results


def get_market_imports(
    client: SpaceTradersClient, system: str, waypoint: str
) -> List[str]:
    """Get list of goods that can be sold at this market"""
    try:
        market_data = client.get_market(system, waypoint)
        return [item["symbol"] for item in market_data["data"]["imports"]]
    except ApiError as e:
        print(f"Failed to get market data: {str(e)}")
        return []


def find_market_for_goods(
    client: SpaceTradersClient,
    system: str,
    goods: List[str],
    current_x: int,
    current_y: int,
) -> Optional[Dict[str, Any]]:
    """
    Find nearest market that accepts the specified goods

    Args:
        client: SpaceTraders client
        system: Current system symbol
        goods: List of goods to sell
        current_x: Current x coordinate
        current_y: Current y coordinate

    Returns:
        Market waypoint data if found, None otherwise
    """
    try:
        # Get all waypoints in system
        all_waypoints = []
        page = 1
        while True:
            response = client._make_request(
                "GET", f"systems/{system}/waypoints?page={page}"
            )
            all_waypoints.extend(response["data"])
            if page * 10 >= response["meta"]["total"]:
                break
            page += 1

        # Find markets
        markets = [
            wp
            for wp in all_waypoints
            if any(trait["symbol"] == "MARKETPLACE" for trait in wp.get("traits", []))
        ]

        if not markets:
            print("No markets found in system")
            return None

        # Check each market's imports
        suitable_markets = []
        for market in markets:
            imports = get_market_imports(client, system, market["symbol"])
            # Check if market accepts any of our goods
            if any(good in imports for good in goods):
                suitable_markets.append(market)

        if not suitable_markets:
            print("No markets found that accept our goods")
            return None

        # Find closest suitable market
        def distance(waypoint):
            dx = waypoint["x"] - current_x
            dy = waypoint["y"] - current_y
            return (dx * dx + dy * dy) ** 0.5

        nearest = min(suitable_markets, key=distance)
        print(f"\nFound suitable market at {nearest['symbol']}")
        print(f"Distance: {int(distance(nearest))} units")
        print("Accepted goods:")
        market_imports = get_market_imports(client, system, nearest["symbol"])
        for good in goods:
            if good in market_imports:
                print(f"- {good}")
        return nearest

    except ApiError as e:
        print(f"Failed to find market: {str(e)}")
        return None


def sell_cargo_at_market(
    client: SpaceTradersClient, ship_symbol: str, market_waypoint: str
) -> List[Dict[str, Any]]:
    """
    Sell cargo at a specific market, only selling what the market accepts

    Returns:
        List of successful sale transactions
    """
    results = []
    try:
        # Get market imports
        system = "-".join(market_waypoint.split("-")[:2])
        market_imports = get_market_imports(client, system, market_waypoint)

        # Get cargo
        cargo = client.get_ship_cargo(ship_symbol)

        # Try to sell each item that the market accepts
        for item in cargo["data"]["inventory"]:
            if item["symbol"] in market_imports:
                try:
                    result = client.sell_cargo(
                        ship_symbol, item["symbol"], item["units"]
                    )
                    transaction = result["data"]["transaction"]
                    print(
                        f"Sold {transaction['units']} units of {transaction['tradeSymbol']} "
                        f"for {transaction['totalPrice']} credits"
                    )
                    results.append(result)
                except ApiError as e:
                    print(f"Failed to sell {item['symbol']}: {str(e)}")
            else:
                print(f"Market does not accept {item['symbol']}")

    except ApiError as e:
        print(f"Error during sale: {str(e)}")

    return results


def handle_excess_cargo(
    client: SpaceTradersClient,
    ship_symbol: str,
    contract_resource: str,
    delivery_destination: str,
) -> None:
    """
    Immediately jettison any non-contract resources to make room for contract resources.
    """
    try:
        # Get current cargo
        cargo = client.get_ship_cargo(ship_symbol)
        non_contract_items = [
            {"symbol": item["symbol"], "units": item["units"]}
            for item in cargo["data"]["inventory"]
            if item["symbol"] != contract_resource
        ]

        if not non_contract_items:
            print("No excess resources to jettison.")
            return

        # Get current location and status
        nav = client.get_ship_nav(ship_symbol)
        current_location = nav["data"]["waypointSymbol"]
        current_status = nav["data"]["status"]

        print(f"Current location: {current_location}")
        print(f"Current status: {current_status}")

        # Jettison all non-contract resources
        print("\nJettisoning non-contract resources:")
        for item in non_contract_items:
            try:
                print(f"Jettisoning {item['units']} units of {item['symbol']}...")
                client.jettison_cargo(ship_symbol, item["symbol"], item["units"])
                print(f"Successfully jettisoned {item['symbol']}")
            except ApiError as e:
                print(f"Failed to jettison {item['symbol']}: {str(e)}")

        # Return to delivery destination if needed and not already there
        if current_location != delivery_destination:
            print(f"\nReturning to delivery destination {delivery_destination}...")

            # Ensure in orbit before navigation
            if current_status == "DOCKED":
                print("Entering orbit before navigation...")
                client.orbit_ship(ship_symbol)

            try:
                # Double check location after potential status change
                nav = client.get_ship_nav(ship_symbol)
                current_location = nav["data"]["waypointSymbol"]

                # Only navigate if we're still not at the destination
                if current_location != delivery_destination:
                    nav_result = client.navigate_ship(ship_symbol, delivery_destination)
                    nav_data = nav_result["data"]["nav"]
                    transit_time = calculate_transit_time(nav_data)
                    print(f"Navigation started. Total transit time: {transit_time}")

                    # Wait for arrival
                    wait_for_arrival(client, ship_symbol, nav_data)
                    print("Arrived at delivery destination.")
                else:
                    print("Already at delivery destination.")
            except ApiError as e:
                print(f"Failed to return to delivery destination: {str(e)}")
                raise
        else:
            print("Already at delivery destination.")

    except ApiError as e:
        print(f"Error handling excess cargo: {str(e)}")
        raise MiningError(f"Failed to handle excess cargo: {str(e)}")
    except Exception as e:
        print(f"Error handling excess cargo: {str(e)}")
        raise MiningError(f"Failed to handle excess cargo: {str(e)}")


def mine_for_contract(
    client: SpaceTradersClient,
    ship_symbol: str,
    contract_id: str,
    resource_type: str,
    units_needed: int,
    delivery_destination: str,
) -> List[Dict[str, Any]]:
    """
    Mine specific resources for a contract

    Args:
        client: SpaceTraders client
        ship_symbol: Symbol of the mining ship
        contract_id: ID of the contract
        resource_type: Type of resource to mine
        units_needed: Number of units needed
        delivery_destination: Where to deliver the resources

    Returns:
        List of mining results
    """
    print(f"\nMining for contract {contract_id}")
    print(f"Target: {units_needed} units of {resource_type}")
    print(f"Delivery destination: {delivery_destination}")
    print(f"Using mining ship: {ship_symbol}")

    results = []
    total_mined = 0

    try:
        while total_mined < units_needed:
            # Mine resources with specific target
            mining_results = mine_resources(client, ship_symbol, resource_type)

            # Check what we got
            for result in mining_results:
                extracted_item = result["data"]["extraction"]["yield"]
                if extracted_item["symbol"] == resource_type:
                    total_mined += extracted_item["units"]
                    results.append(result)
                    print(
                        f"Progress: {total_mined}/{units_needed} units of {resource_type}"
                    )
                else:
                    print(
                        f"Extracted {extracted_item['units']} units of {extracted_item['symbol']} (not needed)"
                    )

            # Check cargo
            cargo = client.get_ship_cargo(ship_symbol)
            current_units = sum(item["units"] for item in cargo["data"]["inventory"])
            capacity = cargo["data"]["capacity"]

            print(f"\nCargo status: {current_units}/{capacity} units")

            if current_units >= capacity:
                print("\nCargo full. Handling excess resources...")
                handle_excess_cargo(
                    client, ship_symbol, resource_type, delivery_destination
                )

                # After selling excess, deliver contract resources
                print("\nDelivering contract resources...")
                nav = client.get_ship_nav(ship_symbol)
                current_status = nav["data"]["status"]

                # Ensure in orbit before navigation if needed
                if current_status == "DOCKED":
                    print("Entering orbit before navigation...")
                    client.orbit_ship(ship_symbol)

                # Navigate to delivery destination
                nav_result = client.navigate_ship(ship_symbol, delivery_destination)
                nav_data = nav_result["data"]["nav"]
                transit_time = calculate_transit_time(nav_data)
                print(f"Navigation started. Total transit time: {transit_time}")

                # Wait for arrival
                wait_for_arrival(client, ship_symbol, nav_data)
                print("Arrived at delivery destination.")

                # Dock and deliver
                print("Docking to deliver resources...")
                client.dock_ship(ship_symbol)

                # Deliver contract cargo
                try:
                    deliver_result = client.deliver_contract(
                        contract_id, ship_symbol, resource_type, total_mined
                    )
                    print(f"Delivered {total_mined} units of {resource_type}")
                    total_mined = 0  # Reset counter after delivery
                except ApiError as e:
                    print(f"Failed to deliver cargo: {str(e)}")

                # Return to mining
                print("\nReturning to mining operations...")
                success, asteroid_field = prepare_for_mining(
                    client, ship_symbol, resource_type
                )
                if not success:
                    raise MiningError("Failed to return to mining location")

            # If we're not getting the resource we need, try a different location
            if not results:
                print(
                    "\nNot finding required resource. Will try a different location next cycle."
                )

    except ApiError as e:
        raise MiningError(f"Mining operation failed: {str(e)}")

    return results
