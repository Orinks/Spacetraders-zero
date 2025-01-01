import time
from typing import Any, Dict, List, Optional, Tuple

from client import ApiError, SpaceTradersClient

from .mining import (MiningError, calculate_transit_time, find_command_ship,
                     find_mining_drone, mine_resources, prepare_for_mining,
                     wait_for_arrival, wait_for_cooldown)


class CoordinatedMiningError(Exception):
    """Custom exception for coordinated mining operations"""

    pass


class RateLimiter:
    """Rate limiter that respects SpaceTraders API limits"""

    def __init__(self):
        self.requests = []  # List of timestamps of recent requests
        self.burst_window = 60  # 60 seconds for burst window
        self.burst_limit = 30  # 30 requests per burst window
        self.rate_limit = 2  # 2 requests per second
        self.last_request_time = 0

    def wait_if_needed(self):
        """Wait if necessary to respect rate limits"""
        current_time = time.time()

        # Clean up old requests outside burst window
        self.requests = [
            t for t in self.requests if current_time - t < self.burst_window
        ]

        # Check burst limit
        if len(self.requests) >= self.burst_limit:
            oldest_request = self.requests[0]
            wait_time = oldest_request + self.burst_window - current_time
            if wait_time > 0:
                print(f"Burst limit reached. Waiting {wait_time:.1f} seconds...")
                time.sleep(wait_time)
                # After waiting, clean up old requests again
                current_time = time.time()
                self.requests = [
                    t for t in self.requests if current_time - t < self.burst_window
                ]

        # Check rate limit (2 requests per second)
        time_since_last = current_time - self.last_request_time
        if time_since_last < (1 / self.rate_limit):
            wait_time = (1 / self.rate_limit) - time_since_last
            time.sleep(wait_time)

        # Record this request
        self.requests.append(current_time)
        self.last_request_time = current_time


# Global rate limiter instance
GLOBAL_RATE_LIMITER = RateLimiter()


def ensure_ships_docked(
    client: SpaceTradersClient, ship1_symbol: str, ship2_symbol: str
) -> bool:
    """
    Ensure both ships are docked at the same location.
    Returns True if successful, False otherwise.
    """
    try:
        # Get ship locations and status
        GLOBAL_RATE_LIMITER.wait_if_needed()
        ship1_nav = client.get_ship_nav(ship1_symbol)
        GLOBAL_RATE_LIMITER.wait_if_needed()
        ship2_nav = client.get_ship_nav(ship2_symbol)

        # Check if ships are at the same location
        if ship1_nav["data"]["waypointSymbol"] != ship2_nav["data"]["waypointSymbol"]:
            print("Ships are not at the same location")
            return False

        # Dock ships if needed
        if ship1_nav["data"]["status"] != "DOCKED":
            print(f"Docking {ship1_symbol}...")
            GLOBAL_RATE_LIMITER.wait_if_needed()
            client.dock_ship(ship1_symbol)

        if ship2_nav["data"]["status"] != "DOCKED":
            print(f"Docking {ship2_symbol}...")
            GLOBAL_RATE_LIMITER.wait_if_needed()
            client.dock_ship(ship2_symbol)

        return True

    except ApiError as e:
        if "429" in str(e):
            print("Rate limit hit, waiting before retry...")
            time.sleep(2)
            return ensure_ships_docked(client, ship1_symbol, ship2_symbol)
        print(f"Error ensuring ships are docked: {str(e)}")
        return False


def transfer_cargo_between_ships(
    client: SpaceTradersClient,
    from_ship: str,
    to_ship: str,
    cargo_symbol: Optional[str] = None,
    max_units: Optional[int] = None,
) -> bool:
    """
    Transfer cargo from one ship to another.
    If cargo_symbol is specified, only transfer that type.
    If max_units is specified, only transfer up to that amount.
    Returns True if any cargo was transferred.
    """
    try:
        # Ensure ships are docked at same location
        if not ensure_ships_docked(client, from_ship, to_ship):
            raise CoordinatedMiningError(
                "Ships must be docked at the same location to transfer cargo"
            )

        # Get cargo information with rate limiting
        GLOBAL_RATE_LIMITER.wait_if_needed()
        from_cargo = client.get_ship_cargo(from_ship)
        GLOBAL_RATE_LIMITER.wait_if_needed()
        to_cargo = client.get_ship_cargo(to_ship)

        # Calculate available space in receiving ship
        to_space = to_cargo["data"]["capacity"] - sum(
            item["units"] for item in to_cargo["data"]["inventory"]
        )

        if to_space <= 0:
            print("Receiving ship's cargo is full")
            return False

        # Track remaining units to transfer if max_units is specified
        remaining_units = max_units if max_units is not None else float("inf")

        # Transfer cargo
        transferred = False
        for item in from_cargo["data"]["inventory"]:
            # Skip if we're only transferring a specific cargo type
            if cargo_symbol and item["symbol"] != cargo_symbol:
                continue

            # Calculate how much to transfer
            units_to_transfer = min(item["units"], to_space)
            if remaining_units < float("inf"):
                units_to_transfer = min(units_to_transfer, remaining_units)

            if units_to_transfer <= 0:
                continue

            print(f"Transferring {units_to_transfer} units of {item['symbol']}...")
            max_transfer_retries = 3
            transfer_retry = 0
            while transfer_retry < max_transfer_retries:
                try:
                    GLOBAL_RATE_LIMITER.wait_if_needed()
                    client.transfer_cargo(
                        from_ship, to_ship, item["symbol"], units_to_transfer
                    )
                    break
                except ApiError as e:
                    if "429" in str(e) and transfer_retry < max_transfer_retries - 1:
                        transfer_retry += 1
                        print(
                            f"Rate limit hit during transfer (attempt {transfer_retry}/{max_transfer_retries}), waiting..."
                        )
                        time.sleep(2 * transfer_retry)  # Exponential backoff
                        continue
                    raise

            transferred = True

            # Update remaining space and units
            to_space -= units_to_transfer
            if remaining_units < float("inf"):
                remaining_units -= units_to_transfer

            if to_space <= 0 or remaining_units <= 0:
                break

        return transferred

    except ApiError as e:
        if "429" in str(e):
            print("Rate limit hit during cargo transfer, waiting before retry...")
            time.sleep(2)
            return transfer_cargo_between_ships(
                client, from_ship, to_ship, cargo_symbol, max_units
            )
        print(f"Error transferring cargo: {str(e)}")
        return False


def get_market_data_with_cache(
    client: SpaceTradersClient,
    system: str,
    market_symbol: str,
    market_cache: Dict[str, Any],
    last_request_time: Dict[str, float],
) -> Optional[Dict[str, Any]]:
    """Get market data with caching and rate limiting"""
    try:
        # Check if we have cached data
        if market_symbol in market_cache:
            return market_cache[market_symbol]

        # Rate limiting: ensure at least 500ms between requests
        current_time = time.time()
        if "last_time" in last_request_time:
            time_since_last = current_time - last_request_time["last_time"]
            if time_since_last < 0.5:  # 500ms
                time.sleep(0.5 - time_since_last)

        # Make the request
        market_data = client.get_market(system, market_symbol)
        market_cache[market_symbol] = market_data
        last_request_time["last_time"] = time.time()

        return market_data
    except ApiError as e:
        if "429" in str(e):  # Rate limit error
            print(f"Rate limit hit, waiting before retry...")
            time.sleep(1)  # Wait a second before potential retry
        print(f"Error getting market data for {market_symbol}: {str(e)}")
        return None


def handle_rate_limit(e: ApiError) -> bool:
    """
    Handle rate limit errors.
    Returns True if it was a rate limit error and handled, False otherwise.
    """
    if "429" in str(e):
        print("Rate limit hit, waiting before retry...")
        time.sleep(2)  # Increased wait time for rate limits
        return True
    return False


def with_rate_limit(func):
    """Decorator to apply rate limiting and handle rate limit responses"""
    rate_limiter = RateLimiter()

    def wrapper(*args, **kwargs):
        max_retries = 3
        retry_count = 0

        while retry_count < max_retries:
            try:
                # Wait for rate limit if needed
                rate_limiter.wait_if_needed()

                # Make the request
                return func(*args, **kwargs)

            except ApiError as e:
                error_str = str(e)
                if "429" in error_str:
                    retry_count += 1
                    # Try to get retry-after from headers if available
                    retry_after = 1  # Default to 1 second
                    if "retry-after" in error_str.lower():
                        try:
                            # Extract retry-after value from error message
                            retry_after = int(
                                error_str.split("retry-after: ")[1].split()[0]
                            )
                        except:
                            pass

                    print(
                        f"Rate limit hit (attempt {retry_count}/{max_retries}). "
                        f"Waiting {retry_after} seconds..."
                    )
                    time.sleep(retry_after)

                    if retry_count >= max_retries:
                        print("Max retries reached. Giving up.")
                        raise
                    continue
                raise

    return wrapper


@with_rate_limit
def get_ship_status(client: SpaceTradersClient, ship_symbol: str) -> Dict[str, Any]:
    """Get ship nav status with rate limit handling"""
    return client.get_ship_nav(ship_symbol)


@with_rate_limit
def get_ship_cargo(client: SpaceTradersClient, ship_symbol: str) -> Dict[str, Any]:
    """Get ship cargo with rate limit handling"""
    return client.get_ship_cargo(ship_symbol)


@with_rate_limit
def navigate_ship(
    client: SpaceTradersClient, ship_symbol: str, destination: str
) -> Dict[str, Any]:
    """Navigate ship with rate limit handling"""
    return client.navigate_ship(ship_symbol, destination)


@with_rate_limit
def orbit_ship(client: SpaceTradersClient, ship_symbol: str) -> Dict[str, Any]:
    """Put ship in orbit with rate limit handling"""
    return client.orbit_ship(ship_symbol)


@with_rate_limit
def dock_ship(client: SpaceTradersClient, ship_symbol: str) -> Dict[str, Any]:
    """Dock ship with rate limit handling"""
    return client.dock_ship(ship_symbol)


@with_rate_limit
def get_contracts(client: SpaceTradersClient) -> Dict[str, Any]:
    """Get contracts with rate limit handling"""
    return client.list_contracts()


@with_rate_limit
def deliver_contract(
    client: SpaceTradersClient,
    contract_id: str,
    ship_symbol: str,
    trade_symbol: str,
    units: int,
) -> Dict[str, Any]:
    """Deliver contract with rate limit handling"""
    return client.deliver_contract(contract_id, ship_symbol, trade_symbol, units)


@with_rate_limit
def fulfill_contract(client: SpaceTradersClient, contract_id: str) -> Dict[str, Any]:
    """Fulfill contract with rate limit handling"""
    return client.fulfill_contract(contract_id)


@with_rate_limit
def get_market(
    client: SpaceTradersClient, system: str, waypoint: str
) -> Dict[str, Any]:
    """Get market data with rate limit handling"""
    return client.get_market(system, waypoint)


@with_rate_limit
def jettison_cargo(
    client: SpaceTradersClient, ship_symbol: str, cargo_symbol: str, units: int
) -> Dict[str, Any]:
    """Jettison cargo with rate limit handling"""
    return client.jettison_cargo(ship_symbol, cargo_symbol, units)


@with_rate_limit
def sell_cargo(
    client: SpaceTradersClient, ship_symbol: str, cargo_symbol: str, units: int
) -> Dict[str, Any]:
    """Sell cargo with rate limit handling"""
    return client.sell_cargo(ship_symbol, cargo_symbol, units)


@with_rate_limit
def set_flight_mode(
    client: SpaceTradersClient, ship_symbol: str, flight_mode: str
) -> Dict[str, Any]:
    """Set ship flight mode with rate limit handling"""
    return client._make_request(
        "PATCH", f"my/ships/{ship_symbol}/nav", {"flightMode": flight_mode}
    )


def ensure_valid_navigation_state(
    client: SpaceTradersClient, ship_symbol: str, target_waypoint: str
) -> bool:
    """
    Ensure ship is in a valid state for navigation and the target is valid.
    Returns True if navigation should proceed, False otherwise.
    """
    try:
        # Get current ship status
        nav = get_ship_status(client, ship_symbol)
        current_waypoint = nav["data"]["waypointSymbol"]
        current_status = nav["data"]["status"]
        current_flight_mode = nav["data"]["flightMode"]

        # Don't navigate if already at destination
        if current_waypoint == target_waypoint:
            print(f"Already at destination {target_waypoint}")
            return False

        # Ensure ship is in orbit
        if current_status != "IN_ORBIT":
            print(f"Ship status is {current_status}, entering orbit...")
            try:
                orbit_ship(client, ship_symbol)
                time.sleep(1)  # Wait a moment for orbit status to update
            except ApiError as e:
                if not handle_rate_limit(e):
                    print(f"Failed to enter orbit: {str(e)}")
                return False

        # Set flight mode to CRUISE for navigation
        if current_flight_mode != "CRUISE":
            print(f"Setting flight mode to CRUISE (current: {current_flight_mode})...")
            try:
                set_flight_mode(client, ship_symbol, "CRUISE")
                time.sleep(1)  # Wait a moment for flight mode to update
            except ApiError as e:
                if not handle_rate_limit(e):
                    print(f"Failed to set flight mode: {str(e)}")
                return False

        # Double check status after changes
        nav = get_ship_status(client, ship_symbol)
        if nav["data"]["status"] != "IN_ORBIT":
            print(f"Failed to achieve orbit. Current status: {nav['data']['status']}")
            return False
        if nav["data"]["flightMode"] != "CRUISE":
            print(
                f"Failed to set flight mode. Current mode: {nav['data']['flightMode']}"
            )
            return False

        return True

    except ApiError as e:
        if not handle_rate_limit(e):
            print(f"Error checking navigation state: {str(e)}")
        return False


def debug_ship_status(client: SpaceTradersClient, ship_symbol: str) -> None:
    """Print detailed ship status for debugging"""
    try:
        print(f"\nDEBUG: Checking detailed status for {ship_symbol}...")

        # Get nav status
        nav = get_ship_status(client, ship_symbol)
        print("Navigation Status:")
        print(f"- Location: {nav['data']['waypointSymbol']}")
        print(f"- Status: {nav['data']['status']}")
        print(f"- Flight Mode: {nav['data']['flightMode']}")

        # Get ship details
        ship = client.get_my_ship(ship_symbol)
        print("\nShip Details:")
        print(f"- Frame: {ship['data']['frame']['name']}")
        print(
            f"- Fuel: {ship['data']['fuel']['current']}/{ship['data']['fuel']['capacity']}"
        )
        print(
            f"- Cargo: {ship['data']['cargo']['units']}/{ship['data']['cargo']['capacity']}"
        )

        # Get current waypoint details
        system = nav["data"]["systemSymbol"]
        waypoint = nav["data"]["waypointSymbol"]
        waypoint_data = client.get_waypoint(system, waypoint)
        print("\nCurrent Waypoint Details:")
        print(f"- Type: {waypoint_data['data']['type']}")
        print(
            f"- Coordinates: ({waypoint_data['data']['x']}, {waypoint_data['data']['y']})"
        )
        print("- Traits:")
        for trait in waypoint_data["data"].get("traits", []):
            print(f"  * {trait['name']}: {trait['description']}")

    except ApiError as e:
        print(f"Error getting debug status: {str(e)}")


class CoordinatedMiningState:
    """State management for coordinated mining to reduce API calls"""

    def __init__(self):
        self.waypoints_cache: Dict[str, List[Dict[str, Any]]] = (
            {}
        )  # Cache of system waypoints
        self.market_cache: Dict[str, Dict[str, Any]] = {}  # Cache of market data
        self.ship_status_cache: Dict[str, Dict[str, Any]] = {}  # Cache of ship status
        self.ship_cargo_cache: Dict[str, Dict[str, Any]] = {}  # Cache of ship cargo
        self.asteroid_field_cache: Dict[str, Dict[str, Any]] = (
            {}
        )  # Cache of asteroid field data
        self.last_update_time: Dict[str, float] = (
            {}
        )  # Track last update time for each cache
        self.cache_duration = 30  # Cache duration in seconds

    def is_cache_valid(self, cache_key: str) -> bool:
        """Check if cache is still valid"""
        if cache_key not in self.last_update_time:
            return False
        return (time.time() - self.last_update_time[cache_key]) < self.cache_duration

    def update_cache(self, cache_key: str):
        """Update cache timestamp"""
        self.last_update_time[cache_key] = time.time()

    def clear_ship_cache(self, ship_symbol: str):
        """Clear cached data for a specific ship"""
        if ship_symbol in self.ship_status_cache:
            del self.ship_status_cache[ship_symbol]
        if ship_symbol in self.ship_cargo_cache:
            del self.ship_cargo_cache[ship_symbol]

    def get_ship_status(
        self, client: SpaceTradersClient, ship_symbol: str
    ) -> Dict[str, Any]:
        """Get ship status with caching"""
        if ship_symbol in self.ship_status_cache and self.is_cache_valid(
            f"ship_status_{ship_symbol}"
        ):
            return self.ship_status_cache[ship_symbol]

        status = get_ship_status(client, ship_symbol)
        self.ship_status_cache[ship_symbol] = status
        self.update_cache(f"ship_status_{ship_symbol}")
        return status

    def get_ship_cargo(
        self, client: SpaceTradersClient, ship_symbol: str
    ) -> Dict[str, Any]:
        """Get ship cargo with caching"""
        if ship_symbol in self.ship_cargo_cache and self.is_cache_valid(
            f"ship_cargo_{ship_symbol}"
        ):
            return self.ship_cargo_cache[ship_symbol]

        cargo = get_ship_cargo(client, ship_symbol)
        self.ship_cargo_cache[ship_symbol] = cargo
        self.update_cache(f"ship_cargo_{ship_symbol}")
        return cargo

    def get_system_waypoints(
        self, client: SpaceTradersClient, system: str
    ) -> List[Dict[str, Any]]:
        """Get system waypoints with caching"""
        if system in self.waypoints_cache and self.is_cache_valid(
            f"waypoints_{system}"
        ):
            return self.waypoints_cache[system]

        all_waypoints = []
        page = 1
        while True:
            try:
                response = client._make_request(
                    "GET", f"systems/{system}/waypoints?page={page}"
                )
                all_waypoints.extend(response["data"])
                if page * 10 >= response["meta"]["total"]:
                    break
                page += 1
                time.sleep(0.5)  # Rate limiting
            except ApiError as e:
                if "429" in str(e):
                    time.sleep(2)
                    continue
                raise

        self.waypoints_cache[system] = all_waypoints
        self.update_cache(f"waypoints_{system}")
        return all_waypoints


def ensure_ship_ready_for_navigation(client, ship_symbol):
    """Ensure ship is in orbit and has enough fuel for navigation."""
    ship = client.get_my_ship(ship_symbol)
    nav = ship["data"]["nav"]
    fuel = ship["data"]["fuel"]

    # Check if fuel is low (less than 20%)
    if fuel["current"] < fuel["capacity"] * 0.2:
        print(
            f"Fuel is low ({fuel['current']}/{fuel['capacity']}). Docking to refuel..."
        )
        client.dock_ship(ship_symbol)
        refuel_result = client.refuel_ship(ship_symbol)
        print(
            f"Refueled ship. Cost: {refuel_result['data']['transaction']['totalPrice']} credits"
        )
        client.orbit_ship(ship_symbol)

    # Ensure ship is in orbit
    if nav["status"] != "IN_ORBIT":
        print(f"Ship is {nav['status']}. Moving to orbit...")
        if nav["status"] == "DOCKED":
            client.orbit_ship(ship_symbol)
        else:
            # Wait for any in-progress navigation to complete
            wait_for_arrival(client, ship_symbol)
            client.orbit_ship(ship_symbol)

    # Ensure flight mode is CRUISE
    if nav["flightMode"] != "CRUISE":
        print(f"Setting flight mode to CRUISE...")
        client._make_request(
            "PATCH", f"my/ships/{ship_symbol}/nav", {"flightMode": "CRUISE"}
        )


def navigate_to_waypoint(client, ship_symbol, waypoint):
    """Navigate to a waypoint, ensuring the ship is ready first."""
    ensure_ship_ready_for_navigation(client, ship_symbol)
    print(f"Navigating to {waypoint}...")
    nav_result = client.navigate_ship(ship_symbol, waypoint)
    wait_for_arrival(client, ship_symbol, nav_result["data"]["nav"])
    return nav_result


def get_contract_resource_needs(
    client: SpaceTradersClient, contract_id: str
) -> List[Dict[str, Any]]:
    """Get the remaining resources needed for a contract."""
    try:
        GLOBAL_RATE_LIMITER.wait_if_needed()
        contract = client.get_contract(contract_id)
        needed_resources = []

        for delivery in contract["data"]["terms"]["deliver"]:
            remaining_units = delivery["unitsRequired"] - delivery["unitsFulfilled"]
            if remaining_units > 0:
                needed_resources.append(
                    {
                        "symbol": delivery["tradeSymbol"],
                        "units_needed": remaining_units,
                        "destination": delivery["destinationSymbol"],
                    }
                )

        return needed_resources
    except ApiError as e:
        print(f"Error getting contract needs: {str(e)}")
        return []


def get_active_contract(client: SpaceTradersClient) -> Optional[str]:
    """Get the active contract ID if one exists."""
    try:
        GLOBAL_RATE_LIMITER.wait_if_needed()
        contracts = client.list_contracts()
        # Find the first active and accepted contract
        for contract in contracts["data"]:
            if contract["accepted"] and not contract["fulfilled"]:
                return contract["id"]
        return None
    except ApiError as e:
        print(f"Error getting contract: {str(e)}")
        return None


class MiningSession:
    """Track mining session statistics"""

    def __init__(self):
        self.start_time = time.time()
        self.total_mined = {}  # {resource_symbol: units}
        self.total_delivered = {}  # {resource_symbol: units}
        self.contracts_completed = 0
        self.credits_earned = 0

    def add_mined_resource(self, symbol: str, units: int):
        """Track mined resources"""
        self.total_mined[symbol] = self.total_mined.get(symbol, 0) + units

    def add_delivered_resource(self, symbol: str, units: int):
        """Track delivered resources"""
        self.total_delivered[symbol] = self.total_delivered.get(symbol, 0) + units

    def add_contract_completed(self, credits_earned: int):
        """Track completed contract"""
        self.contracts_completed += 1
        self.credits_earned += credits_earned

    def get_session_duration(self) -> str:
        """Get formatted session duration"""
        duration = int(time.time() - self.start_time)
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = duration % 60
        return f"{hours}h {minutes}m {seconds}s"

    def print_summary(self):
        """Print session summary"""
        print("\n" + "=" * 50)
        print("Mining Session Summary")
        print("=" * 50)
        print(f"Session Duration: {self.get_session_duration()}")
        print("\nResources Mined:")
        for symbol, units in self.total_mined.items():
            print(f"- {symbol}: {units} units")
        print("\nResources Delivered:")
        for symbol, units in self.total_delivered.items():
            print(f"- {symbol}: {units} units")
        print(f"\nContracts Completed: {self.contracts_completed}")
        print(f"Credits Earned: {self.credits_earned:,}")
        print("=" * 50)


def coordinate_mining(
    client, command_ship_symbol, mining_drone_symbol, contract_id=None
):
    """Coordinate mining between a command ship and mining drone."""
    print(
        f"Starting coordinated mining with command ship {command_ship_symbol} and mining drone {mining_drone_symbol}"
    )

    # Initialize session tracking
    session = MiningSession()

    # Initialize contract tracking
    active_contract = get_active_contract(client)
    target_resources = []

    if active_contract:
        contract_needs = get_contract_resource_needs(client, active_contract)
        if contract_needs:
            print(f"\nContract {active_contract} needs:")
            for need in contract_needs:
                print(
                    f"- {need['units_needed']} units of {need['symbol']} to be delivered to {need['destination']}"
                )
            target_resources = contract_needs
        else:
            print("No remaining deliveries needed for current contract.")
            active_contract = None
    else:
        print("No active contract found.")

    try:
        while True:
            try:
                # Get ship statuses with rate limiting
                GLOBAL_RATE_LIMITER.wait_if_needed()
                command_ship = client.get_my_ship(command_ship_symbol)
                GLOBAL_RATE_LIMITER.wait_if_needed()
                mining_drone = client.get_my_ship(mining_drone_symbol)

                # Check mining drone cargo status first
                mining_drone_cargo = mining_drone["data"]["cargo"]
                mining_drone_capacity = mining_drone_cargo["capacity"]
                mining_drone_units = mining_drone_cargo["units"]

                # Check command ship cargo status
                command_cargo = command_ship["data"]["cargo"]
                command_capacity = command_cargo["capacity"]
                command_units = command_cargo["units"]

                # If mining drone cargo is full, check if command ship can accept transfer
                if mining_drone_units >= mining_drone_capacity:
                    print(
                        f"Mining drone cargo full ({mining_drone_units}/{mining_drone_capacity})"
                    )

                    # Check if command ship has space
                    available_space = command_capacity - command_units
                    if available_space <= 0:
                        print(
                            f"Command ship cargo full ({command_units}/{command_capacity}). Handling delivery before transfer..."
                        )

                        # If we have an active contract, try to deliver resources
                        if active_contract:
                            print(
                                f"Attempting to deliver resources for contract {active_contract}..."
                            )
                            try:
                                delivered = deliver_contract_resources(
                                    client,
                                    command_ship_symbol,
                                    active_contract,
                                    target_resources,
                                    session,
                                )
                                if delivered:
                                    # Check if we need to get a new contract
                                    if not target_resources:
                                        print(
                                            "Contract completed. Looking for new contract..."
                                        )
                                        active_contract = get_active_contract(client)
                                        if active_contract:
                                            contract_needs = (
                                                get_contract_resource_needs(
                                                    client, active_contract
                                                )
                                            )
                                            if contract_needs:
                                                print(
                                                    f"\nNew contract {active_contract} needs:"
                                                )
                                                for need in contract_needs:
                                                    print(
                                                        f"- {need['units_needed']} units of {need['symbol']} to be delivered to {need['destination']}"
                                                    )
                                                target_resources = contract_needs
                                            else:
                                                print(
                                                    "No deliveries needed for new contract."
                                                )
                                                active_contract = None
                                        else:
                                            print("No new contract found.")
                            except Exception as e:
                                print(f"Failed to deliver contract resources: {str(e)}")
                                if "429" in str(e):
                                    time.sleep(2)

                        # If still full after delivery, try to sell excess at best market
                        GLOBAL_RATE_LIMITER.wait_if_needed()
                        command_ship = client.get_my_ship(command_ship_symbol)
                        command_cargo = command_ship["data"]["cargo"]
                        if command_cargo["units"] > 0:
                            print("Selling excess cargo at best market...")
                            try:
                                sell_cargo_at_best_market(client, command_ship_symbol)
                            except Exception as e:
                                print(f"Failed to sell cargo: {str(e)}")
                                if "429" in str(e):
                                    time.sleep(2)

                        # Skip transfer attempt this iteration
                        print(
                            "Mining drone will remain docked until command ship has space."
                        )
                        time.sleep(5)  # Wait before next iteration
                        continue

                    print("Command ship has space. Proceeding with transfer...")

                    # Navigate command ship to mining drone if needed
                    mining_drone_nav = mining_drone["data"]["nav"]
                    command_ship_nav = command_ship["data"]["nav"]
                    if (
                        command_ship_nav["waypointSymbol"]
                        != mining_drone_nav["waypointSymbol"]
                    ):
                        print(
                            f"Command ship at {command_ship_nav['waypointSymbol']}, navigating to mining drone at {mining_drone_nav['waypointSymbol']}"
                        )
                        try:
                            GLOBAL_RATE_LIMITER.wait_if_needed()
                            navigate_to_waypoint(
                                client,
                                command_ship_symbol,
                                mining_drone_nav["waypointSymbol"],
                            )
                        except ApiError as e:
                            if "429" in str(e):
                                print("Rate limit hit during navigation, waiting...")
                                time.sleep(2)
                                continue
                            raise

                    # Transfer cargo with rate limiting and retries
                    max_transfer_retries = 3
                    transfer_retry = 0
                    transfer_successful = False
                    while transfer_retry < max_transfer_retries:
                        try:
                            transfer_successful = transfer_cargo_between_ships(
                                client, mining_drone_symbol, command_ship_symbol
                            )
                            break
                        except ApiError as e:
                            if (
                                "429" in str(e)
                                and transfer_retry < max_transfer_retries - 1
                            ):
                                transfer_retry += 1
                                print(
                                    f"Rate limit hit during transfer (attempt {transfer_retry}/{max_transfer_retries}), waiting..."
                                )
                                time.sleep(2 * transfer_retry)  # Exponential backoff
                                continue
                            raise

                    # After successful transfer, attempt contract delivery if we have an active contract
                    if transfer_successful and active_contract:
                        print(
                            "Transfer complete. Command ship handling contract delivery while mining drone continues..."
                        )
                        try:
                            GLOBAL_RATE_LIMITER.wait_if_needed()
                            command_ship = client.get_my_ship(command_ship_symbol)
                            command_cargo = command_ship["data"]["cargo"]

                            if command_cargo["units"] > 0:
                                print(
                                    f"Attempting to deliver resources for contract {active_contract}..."
                                )
                                try:
                                    delivered = deliver_contract_resources(
                                        client,
                                        command_ship_symbol,
                                        active_contract,
                                        target_resources,
                                        session,
                                    )
                                    if delivered:
                                        # Check if we need to get a new contract
                                        if not target_resources:
                                            print(
                                                "Contract completed. Looking for new contract..."
                                            )
                                            active_contract = get_active_contract(
                                                client
                                            )
                                            if active_contract:
                                                contract_needs = (
                                                    get_contract_resource_needs(
                                                        client, active_contract
                                                    )
                                                )
                                                if contract_needs:
                                                    print(
                                                        f"\nNew contract {active_contract} needs:"
                                                    )
                                                    for need in contract_needs:
                                                        print(
                                                            f"- {need['units_needed']} units of {need['symbol']} to be delivered to {need['destination']}"
                                                        )
                                                    target_resources = contract_needs
                                                else:
                                                    print(
                                                        "No deliveries needed for new contract."
                                                    )
                                                    active_contract = None
                                            else:
                                                print("No new contract found.")
                                except Exception as e:
                                    print(
                                        f"Failed to deliver contract resources: {str(e)}"
                                    )
                                    if "429" in str(e):
                                        time.sleep(2)
                        except Exception as e:
                            print(
                                f"Error checking command ship after transfer: {str(e)}"
                            )

                # Mining drone continues mining if not full
                if mining_drone_units < mining_drone_capacity:
                    print(
                        f"Mining drone cargo at {mining_drone_units}/{mining_drone_capacity}, continuing mining operations..."
                    )
                    try:
                        # Ensure drone is in orbit for mining
                        if mining_drone["data"]["nav"]["status"] != "IN_ORBIT":
                            GLOBAL_RATE_LIMITER.wait_if_needed()
                            try:
                                client.orbit_ship(mining_drone_symbol)
                            except ApiError as e:
                                if not handle_state_conflict(e):
                                    raise

                        # Start mining operation
                        GLOBAL_RATE_LIMITER.wait_if_needed()
                        try:
                            mining_result = client.extract_resources(
                                mining_drone_symbol
                            )
                        except ApiError as e:
                            if "409" in str(e):
                                if "must be in orbit" in str(e).lower():
                                    print(
                                        "Ship must be in orbit to mine. Entering orbit..."
                                    )
                                    client.orbit_ship(mining_drone_symbol)
                                    mining_result = client.extract_resources(
                                        mining_drone_symbol
                                    )
                                else:
                                    raise
                            elif "429" in str(e):
                                print("Rate limit hit during mining, waiting...")
                                time.sleep(2)
                                continue
                            elif "cooldown" in str(e).lower():
                                print("Mining is on cooldown, waiting...")
                                time.sleep(5)
                                continue
                            else:
                                raise

                        # Print mining results and check against contract needs
                        extraction = mining_result["data"]["extraction"]
                        yield_data = extraction["yield"]
                        print(
                            f"Extracted {yield_data['units']} units of {yield_data['symbol']}"
                        )

                        # Check if this resource is needed for the contract
                        for resource in target_resources:
                            if resource["symbol"] == yield_data["symbol"]:
                                print(
                                    f"This resource is needed for contract delivery! Still need {resource['units_needed']} units."
                                )
                                break

                        # Wait for cooldown
                        cooldown = mining_result["data"]["cooldown"]["remainingSeconds"]
                        if cooldown > 0:
                            print(f"Mining cooldown: {cooldown} seconds")
                            time.sleep(cooldown)

                    except ApiError as e:
                        if "429" in str(e):
                            print("Rate limit hit during mining, waiting...")
                            time.sleep(2)
                        elif "cooldown" in str(e).lower():
                            print("Mining is on cooldown, waiting...")
                            time.sleep(5)
                        else:
                            print(f"Mining error: {str(e)}")
                            time.sleep(5)

                # Sleep briefly between iterations
                time.sleep(1)

                # Update session stats for mining
                if "mining_result" in locals():
                    yield_data = mining_result["data"]["extraction"]["yield"]
                    session.add_mined_resource(
                        yield_data["symbol"], yield_data["units"]
                    )

                # Update session stats for delivery
                if "deliver_result" in locals():
                    delivery = deliver_result["data"]["cargo"]
                    session.add_delivered_resource(
                        delivery["tradeSymbol"], delivery["units"]
                    )

                # Update session stats for contract completion
                if "fulfill_result" in locals():
                    payment = fulfill_result["data"]["contract"]["terms"]["payment"]
                    session.add_contract_completed(payment["onFulfilled"])

                # Clear the local variables to avoid double counting
                if "mining_result" in locals():
                    del mining_result
                if "deliver_result" in locals():
                    del deliver_result
                if "fulfill_result" in locals():
                    del fulfill_result

            except Exception as e:
                print(f"Error in mining coordination: {str(e)}")
                if "429" in str(e):
                    print("Rate limit hit, waiting before retry...")
                    time.sleep(2)
                else:
                    time.sleep(5)  # Wait longer for non-rate-limit errors
                continue

    except KeyboardInterrupt:
        print("\nGracefully shutting down mining operation...")
        session.print_summary()
        print("\nMining operation terminated by user.")
        return
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        session.print_summary()
        raise


def find_best_market_for_cargo(
    client: SpaceTradersClient, ship_symbol: str, cargo_symbol: str
) -> Optional[str]:
    """Find the best market to sell a specific cargo type."""
    try:
        # Get current ship location
        ship = client.get_my_ship(ship_symbol)
        current_system = ship["data"]["nav"]["systemSymbol"]

        # Get all waypoints in the system
        waypoints = []
        page = 1
        while True:
            response = client._make_request(
                "GET", f"systems/{current_system}/waypoints?page={page}"
            )
            waypoints.extend(response["data"])
            if page * 20 >= response["meta"]["total"]:
                break
            page += 1
            time.sleep(0.5)  # Rate limiting

        # Find markets
        best_price = 0
        best_market = None

        for waypoint in waypoints:
            if any(
                trait["symbol"] == "MARKETPLACE" for trait in waypoint.get("traits", [])
            ):
                try:
                    market = client.get_market(current_system, waypoint["symbol"])
                    market_data = market["data"]

                    # First check if this market imports our cargo
                    imports = [
                        item["symbol"] for item in market_data.get("imports", [])
                    ]
                    if cargo_symbol in imports:
                        # If it's an import, we know they'll buy it
                        # Check trade goods for price if available
                        for trade_good in market_data.get("tradeGoods", []):
                            if trade_good["symbol"] == cargo_symbol:
                                if trade_good.get("sellPrice", 0) > best_price:
                                    best_price = trade_good["sellPrice"]
                                    best_market = waypoint["symbol"]
                                break
                        # If we found it in imports but not in trade goods, still consider it
                        if not best_market:
                            best_market = waypoint["symbol"]

                except ApiError:
                    continue
                time.sleep(0.5)  # Rate limiting

        return best_market
    except ApiError as e:
        print(f"Error finding market: {str(e)}")
        return None


def sell_cargo_at_best_market(client: SpaceTradersClient, ship_symbol: str) -> None:
    """Sell all cargo at the best available markets. Jettison cargo that cannot be sold."""
    try:
        # Get ship's cargo
        ship = client.get_my_ship(ship_symbol)
        cargo = ship["data"]["cargo"]

        if cargo["units"] == 0:
            print("No cargo to sell")
            return

        # Try to sell each cargo type at the best market
        for item in cargo["inventory"]:
            print(
                f"\nFinding best market for {item['units']} units of {item['symbol']}..."
            )

            best_market = find_best_market_for_cargo(
                client, ship_symbol, item["symbol"]
            )
            if not best_market:
                print(f"No market found for {item['symbol']}, jettisoning cargo...")
                try:
                    result = client.jettison_cargo(
                        ship_symbol, item["symbol"], item["units"]
                    )
                    print(f"Jettisoned {item['units']} units of {item['symbol']}")
                except ApiError as e:
                    print(f"Failed to jettison {item['symbol']}: {str(e)}")
                continue

            print(f"Best market found at {best_market}")

            # Navigate to market if needed
            current_location = ship["data"]["nav"]["waypointSymbol"]
            if current_location != best_market:
                print(f"Navigating to {best_market}...")
                navigate_to_waypoint(client, ship_symbol, best_market)

            # Dock and sell
            print("Docking at market...")
            client.dock_ship(ship_symbol)

            try:
                result = client.sell_cargo(ship_symbol, item["symbol"], item["units"])
                transaction = result["data"]["transaction"]
                print(
                    f"Sold {transaction['units']} units of {transaction['tradeSymbol']} "
                    f"for {transaction['totalPrice']} credits"
                )
            except ApiError as e:
                print(f"Failed to sell {item['symbol']}, attempting to jettison...")
                try:
                    result = client.jettison_cargo(
                        ship_symbol, item["symbol"], item["units"]
                    )
                    print(f"Jettisoned {item['units']} units of {item['symbol']}")
                except ApiError as e2:
                    print(f"Failed to jettison {item['symbol']}: {str(e2)}")
                continue

    except ApiError as e:
        print(f"Error selling cargo: {str(e)}")


def deliver_contract_resources(
    client: SpaceTradersClient,
    ship_symbol: str,
    contract_id: str,
    target_resources: Optional[List[Dict[str, Any]]] = None,
    session: Optional[MiningSession] = None,
) -> bool:
    """
    Deliver resources for a contract from a ship.
    Returns True if any resources were delivered successfully.
    """
    try:
        # Get contract details and ship cargo
        contract = client.get_contract(contract_id)
        ship_cargo = client.get_ship_cargo(ship_symbol)
        ship_nav = client.get_ship_nav(ship_symbol)

        # Track if we delivered anything
        delivered_something = False

        # Check each delivery requirement
        for delivery in contract["data"]["terms"]["deliver"]:
            # Calculate remaining units needed
            remaining_units = delivery["unitsRequired"] - delivery.get(
                "unitsFulfilled", 0
            )
            if remaining_units <= 0:
                continue

            # Check if we have this resource in cargo
            cargo_item = next(
                (
                    item
                    for item in ship_cargo["data"]["inventory"]
                    if item["symbol"] == delivery["tradeSymbol"]
                ),
                None,
            )

            if not cargo_item:
                continue

            # Calculate how much we can deliver
            units_to_deliver = min(cargo_item["units"], remaining_units)
            if units_to_deliver <= 0:
                continue

            # Navigate to delivery destination if needed
            if ship_nav["data"]["waypointSymbol"] != delivery["destinationSymbol"]:
                print(
                    f"Navigating to delivery destination {delivery['destinationSymbol']}..."
                )
                try:
                    # Use navigate_to_waypoint which handles orbit and navigation
                    navigate_to_waypoint(
                        client, ship_symbol, delivery["destinationSymbol"]
                    )

                    # Get updated nav status after arrival
                    ship_nav = client.get_ship_nav(ship_symbol)
                except ApiError as e:
                    if not handle_state_conflict(e):
                        print(f"Navigation failed: {str(e)}")
                        continue

            # Ensure ship is docked
            if ship_nav["data"]["status"] != "DOCKED":
                try:
                    print("Docking ship for delivery...")
                    client.dock_ship(ship_symbol)
                    time.sleep(1)  # Wait a moment for dock status to update
                except ApiError as e:
                    if not handle_state_conflict(e):
                        print(f"Failed to dock: {str(e)}")
                        continue

            # Double check we're at the right place and docked
            ship_nav = client.get_ship_nav(ship_symbol)
            if (
                ship_nav["data"]["status"] != "DOCKED"
                or ship_nav["data"]["waypointSymbol"] != delivery["destinationSymbol"]
            ):
                print("Ship not in correct state for delivery. Skipping...")
                continue

            # Attempt delivery
            try:
                print(
                    f"Delivering {units_to_deliver} units of {delivery['tradeSymbol']}..."
                )
                deliver_result = client.deliver_contract(
                    contract_id, ship_symbol, delivery["tradeSymbol"], units_to_deliver
                )
                print(
                    f"Successfully delivered {units_to_deliver} units of {delivery['tradeSymbol']}"
                )
                delivered_something = True

                # Track delivery in session if provided
                if session is not None:
                    session.add_delivered_resource(
                        delivery["tradeSymbol"], units_to_deliver
                    )

                # Update target_resources if provided
                if target_resources is not None:
                    # Get updated contract info
                    updated_contract = client.get_contract(contract_id)
                    # Update target_resources with new requirements
                    target_resources.clear()
                    for updated_delivery in updated_contract["data"]["terms"][
                        "deliver"
                    ]:
                        updated_remaining = updated_delivery[
                            "unitsRequired"
                        ] - updated_delivery.get("unitsFulfilled", 0)
                        if updated_remaining > 0:
                            target_resources.append(
                                {
                                    "symbol": updated_delivery["tradeSymbol"],
                                    "units_needed": updated_remaining,
                                    "destination": updated_delivery[
                                        "destinationSymbol"
                                    ],
                                }
                            )

                # Check if contract is fulfilled
                contract = client.get_contract(contract_id)
                if all(
                    item.get("unitsFulfilled", 0) >= item["unitsRequired"]
                    for item in contract["data"]["terms"]["deliver"]
                ):
                    print("\nAll deliveries complete. Fulfilling contract...")
                    try:
                        fulfill_result = client.fulfill_contract(contract_id)
                        payment = fulfill_result["data"]["contract"]["terms"]["payment"]
                        print(
                            f"Contract fulfilled! Received {payment['onFulfilled']} credits"
                        )

                        # Track contract completion in session if provided
                        if session is not None:
                            session.add_contract_completed(payment["onFulfilled"])

                    except ApiError as e:
                        if not handle_state_conflict(e):
                            print(f"Failed to fulfill contract: {str(e)}")

            except ApiError as e:
                if "409" in str(e):
                    if "must be docked" in str(e).lower():
                        print("Ship must be docked for delivery. Attempting to dock...")
                        try:
                            client.dock_ship(ship_symbol)
                            # Retry delivery
                            deliver_result = client.deliver_contract(
                                contract_id,
                                ship_symbol,
                                delivery["tradeSymbol"],
                                units_to_deliver,
                            )
                            print(
                                f"Successfully delivered {units_to_deliver} units of {delivery['tradeSymbol']}"
                            )
                            delivered_something = True

                            # Track delivery in session if provided
                            if session is not None:
                                session.add_delivered_resource(
                                    delivery["tradeSymbol"], units_to_deliver
                                )

                        except ApiError as e2:
                            if not handle_state_conflict(e2):
                                print(f"Delivery failed: {str(e2)}")
                                continue
                    else:
                        print(f"Delivery failed: {str(e)}")
                        continue
                else:
                    print(f"Delivery failed: {str(e)}")
                    continue

        return delivered_something

    except Exception as e:
        print(f"Error in contract delivery: {str(e)}")
        return False


def handle_state_conflict(e: ApiError) -> bool:
    """
    Handle 409 conflict errors by fixing the ship's state.
    Returns True if it was a conflict error and handled, False otherwise.
    """
    if "409" in str(e):
        print("State conflict detected. Attempting to fix...")
        if "must be docked" in str(e).lower():
            return True
        elif "must be in orbit" in str(e).lower():
            return True
        elif "already in orbit" in str(e).lower():
            return True
        elif "already docked" in str(e).lower():
            return True
        elif "in transit" in str(e).lower():
            return True
    return False
