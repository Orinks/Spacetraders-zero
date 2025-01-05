import requests
from src.exceptions import (
    SpaceTradersError,
    AuthenticationError,
    NetworkError,
    ValidationError,
    ResourceNotFoundError,
    CooldownError,
    InsufficientResourcesError,
)


class SpaceTradersClient:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.spacetraders.io/v2"
        self.headers = {"Authorization": f"Bearer {token}"}

    def _make_request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            if method == "GET":
                response = requests.get(url, headers=self.headers, params=params)
            elif method == "POST":
                response = requests.post(url, headers=self.headers, json=data)
            else:
                raise SpaceTradersError(f"Unsupported method: {method}")

            if response.status_code == 401:
                raise AuthenticationError("Invalid token")
            if response.status_code != 200 and response.status_code != 201:
                raise SpaceTradersError(f"API Error: {response.status_code} - {response.text}")
            
            return response.json()
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {str(e)}")

    def get_status(self):
        return self._make_request("GET", "game/status")

    def get_agent(self):
        return self._make_request("GET", "my/agent")

    def list_ships(self):
        """Get a list of all ships owned by the authenticated agent."""
        return self._make_request("GET", "my/ships")

    def get_my_ship(self, ship_symbol):
        """Get details of a specific ship by its symbol."""
        return self._make_request("GET", f"my/ships/{ship_symbol}")

    @staticmethod
    def register_new_agent(symbol, faction):
        url = "https://api.spacetraders.io/v2/register"
        data = {"symbol": symbol, "faction": faction}
        try:
            response = requests.post(url, json=data)
            if response.status_code == 400:
                raise ValidationError(response.json().get("error", {}).get("message", "Invalid input"))
            if response.status_code != 201:
                raise SpaceTradersError(f"Registration failed: {response.text}")
            return response.json()
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error during registration: {str(e)}")

    def list_systems(self, limit: int = 20, page: int = 1):
        """
        Fetch a paginated list of all systems in the game.
        
        Args:
            limit (int): Number of systems to return per page (default: 20)
            page (int): Page number for pagination (default: 1)
            
        Returns:
            dict: Paginated response containing system data
        """
        params = {"limit": limit, "page": page}
        return self._make_request("GET", "systems", params=params)

    def get_system(self, system_symbol: str):
        """
        Get the details of a specific system.
        
        Args:
            system_symbol (str): The symbol of the system to get
            
        Returns:
            dict: System details
        """
        return self._make_request("GET", f"systems/{system_symbol}")

    def list_waypoints(self, system_symbol: str, limit: int = 20, page: int = 1):
        """
        Fetch a paginated list of waypoints in a system.
        
        Args:
            system_symbol (str): The symbol of the system to get waypoints for
            limit (int): Number of waypoints to return per page (default: 20)
            page (int): Page number for pagination (default: 1)
            
        Returns:
            dict: Paginated response containing waypoint data
        """
        params = {"limit": limit, "page": page}
        return self._make_request("GET", f"systems/{system_symbol}/waypoints", params=params)

    def get_waypoint(self, system_symbol: str, waypoint_symbol: str):
        """
        Get the details of a specific waypoint in a system.
        
        Args:
            system_symbol (str): The symbol of the system the waypoint is in
            waypoint_symbol (str): The symbol of the waypoint to get
            
        Returns:
            dict: Waypoint details
        """
        return self._make_request("GET", f"systems/{system_symbol}/waypoints/{waypoint_symbol}")

    def get_market(self, system_symbol: str, waypoint_symbol: str):
        """
        Get market information for a waypoint that contains a marketplace.
        
        Args:
            system_symbol (str): The symbol of the system the market is in
            waypoint_symbol (str): The symbol of the waypoint containing the market
            
        Returns:
            dict: Market details including available goods, prices, and trade volume
        """
        return self._make_request("GET", f"systems/{system_symbol}/waypoints/{waypoint_symbol}/market")

    def get_shipyard(self, system_symbol: str, waypoint_symbol: str):
        """
        Get shipyard information for a waypoint that contains a shipyard.
        
        Args:
            system_symbol (str): The symbol of the system the shipyard is in
            waypoint_symbol (str): The symbol of the waypoint containing the shipyard
            
        Returns:
            dict: Shipyard details including available ships and prices
        """
        return self._make_request("GET", f"systems/{system_symbol}/waypoints/{waypoint_symbol}/shipyard")

    def list_factions(self, limit: int = 20, page: int = 1):
        """
        Fetch a paginated list of all factions in the game.
        
        Args:
            limit (int): Number of factions to return per page (default: 20)
            page (int): Page number for pagination (default: 1)
            
        Returns:
            dict: Paginated response containing faction data including their traits and headquarters
        """
        params = {"limit": limit, "page": page}
        return self._make_request("GET", "factions", params=params)

    def get_faction(self, faction_symbol: str):
        """
        Get the details of a specific faction.
        
        Args:
            faction_symbol (str): The symbol of the faction to get
            
        Returns:
            dict: Faction details including traits, headquarters, and other characteristics
        """
        return self._make_request("GET", f"factions/{faction_symbol}")

    def list_contracts(self, limit: int = 20, page: int = 1):
        """
        Fetch a paginated list of all contracts available to the agent.
        
        Args:
            limit (int): Number of contracts to return per page (default: 20)
            page (int): Page number for pagination (default: 1)
            
        Returns:
            dict: Paginated response containing contract data
        """
        params = {"limit": limit, "page": page}
        return self._make_request("GET", "my/contracts", params=params)

    def get_contract(self, contract_id: str):
        """
        Get the details of a specific contract.
        
        Args:
            contract_id (str): The ID of the contract to get
            
        Returns:
            dict: Contract details including terms, deadlines, and payment information
        """
        return self._make_request("GET", f"my/contracts/{contract_id}")

    def accept_contract(self, contract_id: str):
        """
        Accept a contract, making it available for fulfillment.
        
        Args:
            contract_id (str): The ID of the contract to accept
            
        Returns:
            dict: Updated contract details
        """
        return self._make_request("POST", f"my/contracts/{contract_id}/accept")

    def deliver_contract(self, contract_id: str, ship_symbol: str, trade_symbol: str, units: int):
        """
        Deliver cargo to fulfill a contract.
        
        Args:
            contract_id (str): The ID of the contract
            ship_symbol (str): The symbol of the ship delivering the cargo
            trade_symbol (str): The symbol of the trade good to deliver
            units (int): The number of units to deliver
            
        Returns:
            dict: Updated contract details
        """
        data = {
            "shipSymbol": ship_symbol,
            "tradeSymbol": trade_symbol,
            "units": units
        }
        return self._make_request("POST", f"my/contracts/{contract_id}/deliver", data=data)

    def fulfill_contract(self, contract_id: str):
        """
        Fulfill a contract after all requirements have been met.
        
        Args:
            contract_id (str): The ID of the contract to fulfill
            
        Returns:
            dict: Final contract details including payment
        """
        return self._make_request("POST", f"my/contracts/{contract_id}/fulfill")

    def purchase_ship(self, ship_type: str, waypoint_symbol: str):
        """
        Purchase a ship at a shipyard.
        
        Args:
            ship_type (str): The type of ship to purchase
            waypoint_symbol (str): The symbol of the waypoint containing the shipyard
            
        Returns:
            dict: Details of the purchased ship
        """
        data = {
            "shipType": ship_type,
            "waypointSymbol": waypoint_symbol
        }
        return self._make_request("POST", "my/ships", data=data)

    def get_ship_nav(self, ship_symbol: str):
        """
        Get the current navigation details of a ship.
        
        Args:
            ship_symbol (str): The symbol of the ship
            
        Returns:
            dict: Navigation details including current route, status, and flight mode
        """
        return self._make_request("GET", f"my/ships/{ship_symbol}/nav")

    def orbit_ship(self, ship_symbol: str):
        """
        Attempt to move your ship into orbit at its current location.
        
        Args:
            ship_symbol (str): The symbol of the ship to orbit
            
        Returns:
            dict: Updated navigation details
        """
        return self._make_request("POST", f"my/ships/{ship_symbol}/orbit")

    def dock_ship(self, ship_symbol: str):
        """
        Attempt to dock your ship at its current location.
        
        Args:
            ship_symbol (str): The symbol of the ship to dock
            
        Returns:
            dict: Updated navigation details
        """
        return self._make_request("POST", f"my/ships/{ship_symbol}/dock")

    def navigate_ship(self, ship_symbol: str, waypoint_symbol: str):
        """
        Navigate your ship to a target destination.
        
        Args:
            ship_symbol (str): The symbol of the ship to navigate
            waypoint_symbol (str): The symbol of the waypoint to navigate to
            
        Returns:
            dict: Navigation details including route and fuel consumption
        """
        data = {
            "waypointSymbol": waypoint_symbol
        }
        return self._make_request("POST", f"my/ships/{ship_symbol}/navigate", data=data)

    def patch_ship_nav(self, ship_symbol: str, flight_mode: str):
        """
        Update the flight mode of a ship.
        
        Args:
            ship_symbol (str): The symbol of the ship to update
            flight_mode (str): The new flight mode. 
                             One of: 'DRIFT', 'STEALTH', 'CRUISE', 'BURN'
            
        Returns:
            dict: Updated navigation details
        """
        data = {
            "flightMode": flight_mode
        }
        return self._make_request("PATCH", f"my/ships/{ship_symbol}/nav", data=data)

    def get_ship_cargo(self, ship_symbol: str):
        """
        Get the cargo details of a ship.
        
        Args:
            ship_symbol (str): The symbol of the ship
            
        Returns:
            dict: Cargo details including inventory and capacity
        """
        return self._make_request("GET", f"my/ships/{ship_symbol}/cargo")

    def purchase_cargo(self, ship_symbol: str, symbol: str, units: int):
        """
        Purchase cargo from a market.
        
        Args:
            ship_symbol (str): The symbol of the ship to purchase cargo for
            symbol (str): The symbol of the trade good to purchase
            units (int): The number of units to purchase
            
        Returns:
            dict: Updated cargo details and transaction information
        """
        data = {
            "symbol": symbol,
            "units": units
        }
        return self._make_request("POST", f"my/ships/{ship_symbol}/purchase", data=data)

    def sell_cargo(self, ship_symbol: str, symbol: str, units: int):
        """
        Sell cargo to a market.
        
        Args:
            ship_symbol (str): The symbol of the ship selling cargo
            symbol (str): The symbol of the trade good to sell
            units (int): The number of units to sell
            
        Returns:
            dict: Updated cargo details and transaction information
        """
        data = {
            "symbol": symbol,
            "units": units
        }
        return self._make_request("POST", f"my/ships/{ship_symbol}/sell", data=data)

    def transfer_cargo(self, ship_symbol: str, trade_symbol: str, units: int, receiving_ship: str):
        """
        Transfer cargo between ships.
        
        Args:
            ship_symbol (str): The symbol of the ship transferring cargo
            trade_symbol (str): The symbol of the trade good to transfer
            units (int): The number of units to transfer
            receiving_ship (str): The symbol of the ship receiving the cargo
            
        Returns:
            dict: Updated cargo details for both ships
        """
        data = {
            "tradeSymbol": trade_symbol,
            "units": units,
            "shipSymbol": receiving_ship
        }
        return self._make_request("POST", f"my/ships/{ship_symbol}/transfer", data=data)

    def jettison_cargo(self, ship_symbol: str, symbol: str, units: int):
        """
        Jettison (throw away) cargo from a ship.
        
        Args:
            ship_symbol (str): The symbol of the ship jettisoning cargo
            symbol (str): The symbol of the trade good to jettison
            units (int): The number of units to jettison
            
        Returns:
            dict: Updated cargo details
        """
        data = {
            "symbol": symbol,
            "units": units
        }
        return self._make_request("POST", f"my/ships/{ship_symbol}/jettison", data=data)

    def refuel_ship(self, ship_symbol: str, units: int | None = None):
        """
        Refuel a ship from a market.
        
        Args:
            ship_symbol (str): The symbol of the ship to refuel
            units (int, optional): The amount of fuel to purchase. If not specified,
                                 will refuel to maximum capacity
            
        Returns:
            dict: Updated fuel details and transaction information
        """
        data = {"units": units} if units is not None else {}
        return self._make_request("POST", f"my/ships/{ship_symbol}/refuel", data=data)

    def create_chart(self, ship_symbol: str):
        """
        Create a chart of the current waypoint.
        
        Args:
            ship_symbol (str): The symbol of the ship creating the chart
            
        Returns:
            dict: Details of the chart that was created
        """
        return self._make_request("POST", f"my/ships/{ship_symbol}/chart")

    def create_survey(self, ship_symbol: str):
        """
        Create a survey of deposits at the current waypoint.
        
        Args:
            ship_symbol (str): The symbol of the ship creating the survey
            
        Returns:
            dict: Survey results containing deposits found
        """
        return self._make_request("POST", f"my/ships/{ship_symbol}/survey")

    def extract_resources(self, ship_symbol: str, survey: dict | None = None):
        """
        Extract resources from the current waypoint.
        
        Args:
            ship_symbol (str): The symbol of the ship extracting resources
            survey (dict, optional): Survey data to target specific deposits
            
        Returns:
            dict: Extraction results including yield and cooldown
        """
        data = {"survey": survey} if survey is not None else {}
        return self._make_request("POST", f"my/ships/{ship_symbol}/extract", data=data)

    def create_ship_system_scan(self, ship_symbol: str):
        """
        Scan for system information.
        
        Args:
            ship_symbol (str): The symbol of the ship performing the scan
            
        Returns:
            dict: Results of the scan including nearby systems
        """
        return self._make_request("POST", f"my/ships/{ship_symbol}/scan/systems")

    def create_ship_waypoint_scan(self, ship_symbol: str):
        """
        Scan for waypoint information.
        
        Args:
            ship_symbol (str): The symbol of the ship performing the scan
            
        Returns:
            dict: Results of the scan including nearby waypoints
        """
        return self._make_request("POST", f"my/ships/{ship_symbol}/scan/waypoints")

    def get_mounts(self, ship_symbol: str):
        """
        Get the mounts installed on a ship.
        
        Args:
            ship_symbol (str): The symbol of the ship
            
        Returns:
            dict: List of mounts installed on the ship
        """
        return self._make_request("GET", f"my/ships/{ship_symbol}/mounts")

    def install_mount(self, ship_symbol: str, mount_symbol: str):
        """
        Install a mount on a ship.
        
        Args:
            ship_symbol (str): The symbol of the ship
            mount_symbol (str): The symbol of the mount to install
            
        Returns:
            dict: Updated ship mount information
        """
        data = {
            "symbol": mount_symbol
        }
        return self._make_request("POST", f"my/ships/{ship_symbol}/mounts/install", data=data)

    def remove_mount(self, ship_symbol: str, mount_symbol: str):
        """
        Remove a mount from a ship.
        
        Args:
            ship_symbol (str): The symbol of the ship
            mount_symbol (str): The symbol of the mount to remove
            
        Returns:
            dict: Updated ship mount information
        """
        data = {
            "symbol": mount_symbol
        }
        return self._make_request("POST", f"my/ships/{ship_symbol}/mounts/remove", data=data)
