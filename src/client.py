import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
from dotenv import load_dotenv, set_key
from pydantic import BaseModel


class ApiError(Exception):
    """Custom exception for API errors"""

    pass


class SpaceTradersClient:
    BASE_URL = "https://api.spacetraders.io/v2"

    def __init__(self, token: Optional[str] = None):
        """Initialize the SpaceTraders client with an optional token"""
        load_dotenv()
        self.token = token or os.getenv("SPACETRADERS_TOKEN")
        if not self.token:
            raise ValueError(
                "API token is required. Set it in .env file or pass to constructor."
            )

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def register_new_agent(symbol: str, faction: str = "COSMIC") -> Dict[str, Any]:
        """
        Register a new agent and save the token to .env file

        Args:
            symbol: Unique identifier for your agent (3-14 characters, A-Z, 0-9, -)
            faction: Starting faction (default: COSMIC)

        Returns:
            Dict containing registration response data
        """
        url = f"{SpaceTradersClient.BASE_URL}/register"

        try:
            response = requests.post(url, json={"symbol": symbol, "faction": faction})
            response.raise_for_status()
            data = response.json()

            # Save token to .env file
            token = data["data"]["token"]
            env_path = Path(".env")

            # Create .env file if it doesn't exist
            env_path.touch(exist_ok=True)

            # Save token to .env
            set_key(str(env_path), "SPACETRADERS_TOKEN", token)

            return data

        except requests.exceptions.RequestException as e:
            raise ApiError(f"Registration failed: {str(e)}")

    def _make_request(
        self, method: str, endpoint: str, data: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Make a request to the SpaceTraders API"""
        url = f"{self.BASE_URL}/{endpoint}"

        try:
            response = requests.request(
                method=method, url=url, headers=self.headers, json=data
            )
            if response.status_code == 422:
                error_data = response.json()
                raise ApiError(
                    f"API request failed: {response.status_code} {response.reason} - {error_data.get('error', {}).get('message', 'No details provided')}"
                )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ApiError(f"API request failed: {str(e)}")

    def get_agent(self) -> Dict[str, Any]:
        """Get current agent details"""
        return self._make_request("GET", "my/agent")

    def list_contracts(self) -> Dict[str, Any]:
        """List available contracts"""
        return self._make_request("GET", "my/contracts")

    def list_ships(self) -> Dict[str, Any]:
        """List owned ships"""
        return self._make_request("GET", "my/ships")

    def get_system_waypoints(self, system_symbol: str) -> Dict[str, Any]:
        """Get waypoints in a system"""
        return self._make_request("GET", f"systems/{system_symbol}/waypoints")

    def get_market(self, system_symbol: str, waypoint_symbol: str) -> Dict[str, Any]:
        """Get market data for a waypoint"""
        return self._make_request(
            "GET", f"systems/{system_symbol}/waypoints/{waypoint_symbol}/market"
        )

    def navigate_ship(self, ship_symbol: str, waypoint_symbol: str) -> Dict[str, Any]:
        """Navigate ship to waypoint"""
        return self._make_request(
            "POST",
            f"my/ships/{ship_symbol}/navigate",
            {"waypointSymbol": waypoint_symbol},
        )

    def dock_ship(self, ship_symbol: str) -> Dict[str, Any]:
        """Dock ship at current waypoint"""
        return self._make_request("POST", f"my/ships/{ship_symbol}/dock")

    def orbit_ship(self, ship_symbol: str) -> Dict[str, Any]:
        """Move ship to orbit"""
        return self._make_request("POST", f"my/ships/{ship_symbol}/orbit")

    def get_shipyard(self, system_symbol: str, waypoint_symbol: str) -> Dict[str, Any]:
        """Get shipyard data for a waypoint"""
        return self._make_request(
            "GET", f"systems/{system_symbol}/waypoints/{waypoint_symbol}/shipyard"
        )

    def get_waypoint(self, system_symbol: str, waypoint_symbol: str) -> Dict[str, Any]:
        """Get waypoint details"""
        return self._make_request(
            "GET", f"systems/{system_symbol}/waypoints/{waypoint_symbol}"
        )

    def purchase_ship(self, ship_type: str, waypoint_symbol: str) -> Dict[str, Any]:
        """Purchase a ship at the specified waypoint"""
        return self._make_request(
            "POST",
            "my/ships",
            {"shipType": ship_type, "waypointSymbol": waypoint_symbol},
        )

    def get_agent_details(self) -> Dict[str, Any]:
        """Get detailed agent information including credits"""
        return self._make_request("GET", "my/agent")

    def has_ship_type(self, ships_data: List[Dict[str, Any]], ship_type: str) -> bool:
        """Check if agent already owns a specific type of ship"""
        return any(ship["frame"]["symbol"] == ship_type for ship in ships_data)

    def extract_resources(self, ship_symbol: str) -> Dict[str, Any]:
        """Extract resources at current location"""
        return self._make_request("POST", f"my/ships/{ship_symbol}/extract")

    def get_ship_cargo(self, ship_symbol: str) -> Dict[str, Any]:
        """Get ship's cargo details"""
        return self._make_request("GET", f"my/ships/{ship_symbol}/cargo")

    def get_ship_cooldown(self, ship_symbol: str) -> Dict[str, Any]:
        """Get ship's cooldown status"""
        return self._make_request("GET", f"my/ships/{ship_symbol}/cooldown")

    def check_waypoint_sells_fuel(
        self, system_symbol: str, waypoint_symbol: str
    ) -> bool:
        """Check if a waypoint sells fuel"""
        try:
            market = self.get_market(system_symbol, waypoint_symbol)
            return any(
                good["symbol"] == "FUEL"
                for good in market["data"].get("tradeGoods", [])
            )
        except ApiError:
            return False

    def find_shipyards_in_system(self, system_symbol: str) -> List[Dict[str, Any]]:
        """Find all shipyards in the system"""
        try:
            # Get all waypoints with pagination
            all_waypoints = []
            page = 1
            while True:
                response = self._make_request(
                    "GET", f"systems/{system_symbol}/waypoints?page={page}"
                )
                all_waypoints.extend(response["data"])
                if page * 20 >= response["meta"]["total"]:
                    break
                page += 1

            # Look for waypoints with shipyard trait
            shipyards = [
                waypoint
                for waypoint in all_waypoints
                if any(
                    trait["symbol"] == "SHIPYARD"
                    for trait in waypoint.get("traits", [])
                )
            ]

            if shipyards:
                print(f"Found {len(shipyards)} shipyards:")
                for shipyard in shipyards:
                    print(
                        f"- {shipyard['symbol']} at ({shipyard['x']}, {shipyard['y']})"
                    )
            else:
                print("No shipyards found in this system.")

            return shipyards

        except ApiError as e:
            print(f"Error searching for shipyards: {e}")
            return []

    def find_nearest_shipyard(
        self, system_symbol: str, current_x: int, current_y: int
    ) -> Optional[Dict[str, Any]]:
        """Find the nearest shipyard to the given coordinates"""
        shipyards = self.find_shipyards_in_system(system_symbol)
        if not shipyards:
            return None

        # Calculate distances and find the closest
        def distance(waypoint):
            dx = waypoint["x"] - current_x
            dy = waypoint["y"] - current_y
            return (dx * dx + dy * dy) ** 0.5

        return min(shipyards, key=distance)

    def find_fuel_stations_in_system(self, system_symbol: str) -> List[Dict[str, Any]]:
        """Find all fuel stations in the system"""
        try:
            waypoints = []
            page = 1
            while True:
                response = self._make_request(
                    "GET", f"systems/{system_symbol}/waypoints?page={page}"
                )
                waypoints.extend(response["data"])
                if page * 10 >= response["meta"]["total"]:
                    break
                page += 1

            # Look for FUEL_STATION type waypoints
            fuel_stations = [
                waypoint for waypoint in waypoints if waypoint["type"] == "FUEL_STATION"
            ]

            if fuel_stations:
                print(f"Found {len(fuel_stations)} fuel stations:")
                for station in fuel_stations:
                    print(f"- {station['symbol']} at ({station['x']}, {station['y']})")
            else:
                print("No fuel stations found in this system.")

            return fuel_stations

        except ApiError as e:
            print(f"Error searching for fuel stations: {e}")
            return []

    def find_nearest_fuel_station(
        self, system_symbol: str, current_x: int, current_y: int
    ) -> Optional[Dict[str, Any]]:
        """Find the nearest fuel station to the given coordinates"""
        stations = self.find_fuel_stations_in_system(system_symbol)
        if not stations:
            return None

        # Calculate distances and find the closest
        def distance(waypoint):
            dx = waypoint["x"] - current_x
            dy = waypoint["y"] - current_y
            return (dx * dx + dy * dy) ** 0.5

        return min(stations, key=distance)

    def refuel_ship(self, ship_symbol: str) -> Dict[str, Any]:
        """Refuel ship at current waypoint"""
        # Get ship's current location
        nav = self.get_ship_nav(ship_symbol)
        system = nav["data"]["systemSymbol"]
        current_waypoint = nav["data"]["waypointSymbol"]
        status = nav["data"]["status"]

        # Get current coordinates from waypoint details
        waypoint_info = self.get_waypoint(system, current_waypoint)
        current_x = waypoint_info["data"]["x"]
        current_y = waypoint_info["data"]["y"]

        # Check if current waypoint sells fuel
        if self.check_waypoint_sells_fuel(system, current_waypoint):
            if status != "DOCKED":
                self.dock_ship(ship_symbol)
            return self._make_request("POST", f"my/ships/{ship_symbol}/refuel", {})

        # Find nearest fuel station
        print("\nLooking for nearest fuel station...")
        nearest_station = self.find_nearest_fuel_station(system, current_x, current_y)
        if not nearest_station:
            raise ApiError(f"No fuel stations found in system {system}")

        print(f"Found fuel station at {nearest_station['symbol']}")

        # Navigate to fuel station if needed
        if current_waypoint != nearest_station["symbol"]:
            if status != "IN_ORBIT":
                print("Entering orbit...")
                self.orbit_ship(ship_symbol)

            print(f"Navigating to fuel station {nearest_station['symbol']}...")
            self.navigate_ship(ship_symbol, nearest_station["symbol"])

            # Wait for arrival and dock
            print("Docking at fuel station...")
            self.dock_ship(ship_symbol)

        # Attempt to refuel
        return self._make_request("POST", f"my/ships/{ship_symbol}/refuel", {})

    def jettison_cargo(
        self, ship_symbol: str, cargo_symbol: str, units: int
    ) -> Dict[str, Any]:
        """Jettison cargo from ship"""
        return self._make_request(
            "POST",
            f"my/ships/{ship_symbol}/jettison",
            {"symbol": cargo_symbol, "units": units},
        )

    def sell_cargo(
        self, ship_symbol: str, cargo_symbol: str, units: int
    ) -> Dict[str, Any]:
        """Sell cargo at current market"""
        return self._make_request(
            "POST",
            f"my/ships/{ship_symbol}/sell",
            {"symbol": cargo_symbol, "units": units},
        )

    def get_ship_nav(self, ship_symbol: str) -> Dict[str, Any]:
        """Get ship's navigation details"""
        return self._make_request("GET", f"my/ships/{ship_symbol}/nav")

    def get_my_ship(self, ship_symbol: str) -> Dict[str, Any]:
        """Get details about a specific ship"""
        return self._make_request("GET", f"my/ships/{ship_symbol}")

    def find_asteroids_in_system(self, system_symbol: str) -> List[Dict[str, Any]]:
        """Find all asteroid fields in the system"""
        try:
            print(f"Searching for asteroid fields in system {system_symbol}...")
            waypoints = self.get_system_waypoints(system_symbol)

            # Look for both ASTEROID_FIELD type and ASTEROID trait
            asteroid_fields = [
                waypoint
                for waypoint in waypoints["data"]
                if (
                    waypoint["type"] == "ASTEROID_FIELD"
                    or any(
                        trait["symbol"] == "ASTEROID"
                        for trait in waypoint.get("traits", [])
                    )
                )
            ]

            if asteroid_fields:
                print(f"Found {len(asteroid_fields)} potential mining locations:")
                for field in asteroid_fields:
                    print(f"- {field['symbol']} ({field['type']})")
            else:
                print("No asteroid fields found in this system.")

            return asteroid_fields

        except ApiError as e:
            print(f"Error searching for asteroid fields: {e}")
            return []

    def get_contract(self, contract_id: str) -> Dict[str, Any]:
        """Get details of a specific contract"""
        return self._make_request("GET", f"my/contracts/{contract_id}")

    def accept_contract(self, contract_id: str) -> Dict[str, Any]:
        """Accept a contract"""
        return self._make_request("POST", f"my/contracts/{contract_id}/accept")

    def deliver_contract(
        self, contract_id: str, ship_symbol: str, trade_symbol: str, units: int
    ) -> Dict[str, Any]:
        """Deliver contract cargo"""
        return self._make_request(
            "POST",
            f"my/contracts/{contract_id}/deliver",
            {"shipSymbol": ship_symbol, "tradeSymbol": trade_symbol, "units": units},
        )

    def fulfill_contract(self, contract_id: str) -> Dict[str, Any]:
        """Mark a contract as fulfilled"""
        return self._make_request("POST", f"my/contracts/{contract_id}/fulfill")

    def find_engineered_asteroids(self, system_symbol: str) -> List[Dict[str, Any]]:
        """Find engineered asteroids in the system"""
        try:
            print(f"Searching for engineered asteroids in system {system_symbol}...")
            waypoints = self.get_system_waypoints(system_symbol)

            # Look specifically for ENGINEERED_ASTEROID type
            engineered_asteroids = [
                waypoint
                for waypoint in waypoints["data"]
                if waypoint["type"] == "ENGINEERED_ASTEROID"
            ]

            if engineered_asteroids:
                print(f"Found {len(engineered_asteroids)} engineered asteroids:")
                for asteroid in engineered_asteroids:
                    print(
                        f"- {asteroid['symbol']} at ({asteroid['x']}, {asteroid['y']})"
                    )
            else:
                print("No engineered asteroids found in this system.")

            return engineered_asteroids

        except ApiError as e:
            print(f"Error searching for engineered asteroids: {e}")
            return []

    def transfer_cargo(
        self, ship_symbol: str, receiving_ship: str, cargo_symbol: str, units: int
    ) -> Dict[str, Any]:
        """
        Transfer cargo between ships. Ships must be in the same location and both must be docked.

        Args:
            ship_symbol: The symbol of the ship transferring cargo
            receiving_ship: The symbol of the ship receiving cargo
            cargo_symbol: The symbol of the cargo to transfer
            units: The number of units to transfer

        Returns:
            API response containing transfer details
        """
        return self._make_request(
            "POST",
            f"my/ships/{ship_symbol}/transfer",
            {"tradeSymbol": cargo_symbol, "units": units, "shipSymbol": receiving_ship},
        )
