from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass
import time

from src.client import SpaceTradersClient
from .ship_utils import find_nearest_shipyard, purchase_ship


@dataclass
class ExplorationTarget:
    system_symbol: str
    waypoint_symbol: str
    waypoint_type: str
    distance: float
    is_charted: bool = False


class ExplorationManager:
    def __init__(self, client: SpaceTradersClient):
        self.client = client
        self.current_system: Optional[str] = None
        self.explored_waypoints: Set[str] = set()
        self.charted_waypoints: Set[str] = set()
    
    def get_explorer_ship(self) -> Optional[Dict]:
        """Get or purchase an explorer ship for scanning and navigation."""
        ships = self.client.list_ships()
        for ship in ships["data"]:
            if ship["registration"]["role"] == "EXPLORER":
                return ship
                
        # No explorer found, try to purchase one
        if not self.current_system:
            # Get current system from first ship or agent HQ
            try:
                ships = self.client.list_ships()
                if ships["data"]:
                    self.current_system = ships["data"][0]["nav"]["systemSymbol"]
                else:
                    agent = self.client.get_agent()
                    self.current_system = "-".join(agent["data"]["headquarters"].split("-")[:2])
            except Exception as e:
                print(f"Error getting current system: {str(e)}")
                return None
                
        if self.current_system:
            shipyard = find_nearest_shipyard(self.client, self.current_system)
            if shipyard:
                return purchase_ship(self.client, shipyard, "SHIP_EXPLORER")
        return None

    def scan_system(self, ship_symbol: str) -> List[ExplorationTarget]:
        """Scan the current system for waypoints."""
        try:
            # First dock the ship if it's in orbit
            ship_nav = self.client.get_ship_nav(ship_symbol)["data"]
            if ship_nav["status"] == "IN_ORBIT":
                self.client.dock_ship(ship_symbol)
            
            # Use ship's sensor array to scan waypoints
            scan_result = self.client.create_ship_waypoint_scan(ship_symbol)
            waypoints = scan_result["data"]["waypoints"]
            
            exploration_targets = []
            for waypoint in waypoints:
                if waypoint["symbol"] not in self.explored_waypoints:
                    # Calculate rough distance based on x,y coordinates
                    ship_nav = self.client.get_ship_nav(ship_symbol)["data"]
                    current_x = ship_nav["route"]["destination"]["x"]
                    current_y = ship_nav["route"]["destination"]["y"]
                    distance = ((waypoint["x"] - current_x) ** 2 + (waypoint["y"] - current_y) ** 2) ** 0.5
                    
                    target = ExplorationTarget(
                        system_symbol=waypoint["systemSymbol"],
                        waypoint_symbol=waypoint["symbol"],
                        waypoint_type=waypoint["type"],
                        distance=distance,
                        is_charted="chart" in waypoint
                    )
                    exploration_targets.append(target)
            
            return sorted(exploration_targets, key=lambda t: t.distance)
        except Exception as e:
            print(f"Error scanning system: {str(e)}")
            return []

    def navigate_to_waypoint(self, ship_symbol: str, waypoint_symbol: str) -> bool:
        """Navigate to a specific waypoint."""
        try:
            ship_nav = self.client.get_ship_nav(ship_symbol)["data"]
            
            # If not in orbit, enter orbit first
            if ship_nav["status"] == "DOCKED":
                self.client.orbit_ship(ship_symbol)
            
            # Navigate to target waypoint
            result = self.client.navigate_ship(ship_symbol, waypoint_symbol)
            if "error" in result:
                print(f"Navigation error: {result['error']['message']}")
                return False
                
            # Wait for arrival
            while True:
                nav = self.client.get_ship_nav(ship_symbol)["data"]
                if nav["status"] != "IN_TRANSIT":
                    break
                time.sleep(1)
            
            self.explored_waypoints.add(waypoint_symbol)
            return True
            
        except Exception as e:
            print(f"Error navigating to waypoint: {str(e)}")
            return False

    def chart_waypoint(self, ship_symbol: str) -> bool:
        """Create a chart of the current waypoint."""
        try:
            ship_nav = self.client.get_ship_nav(ship_symbol)["data"]
            current_waypoint = ship_nav["waypointSymbol"]
            
            if current_waypoint in self.charted_waypoints:
                return True
                
            # First dock the ship if it's in orbit
            if ship_nav["status"] == "IN_ORBIT":
                self.client.dock_ship(ship_symbol)
            
            # Create chart of the waypoint
            result = self.client.create_chart(ship_symbol)
            if "error" not in result:
                self.charted_waypoints.add(current_waypoint)
                return True
            return False
            
        except Exception as e:
            print(f"Error charting waypoint: {str(e)}")
            return False

    def explore_system(self, ship_symbol: str) -> None:
        """Systematically explore and chart all waypoints in the current system."""
        try:
            # Get ship's current system
            ship_nav = self.client.get_ship_nav(ship_symbol)["data"]
            self.current_system = ship_nav["systemSymbol"]
            
            while True:
                # Scan for unexplored waypoints
                targets = self.scan_system(ship_symbol)
                if not targets:
                    print("No more unexplored waypoints in system")
                    break
                
                # Navigate to closest unexplored waypoint
                target = targets[0]
                print(f"Navigating to {target.waypoint_symbol} ({target.waypoint_type})")
                
                if self.navigate_to_waypoint(ship_symbol, target.waypoint_symbol):
                    if not target.is_charted:
                        print(f"Creating chart of {target.waypoint_symbol}")
                        self.chart_waypoint(ship_symbol)
                
                time.sleep(1)  # Cooldown between actions
                
        except Exception as e:
            print(f"Error during system exploration: {str(e)}") 