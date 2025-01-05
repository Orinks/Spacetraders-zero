import os
from dotenv import load_dotenv

from src.client import SpaceTradersClient
from src.automation.exploration import ExplorationManager


def main():
    # Load environment variables
    load_dotenv()
    token = os.getenv("SPACETRADERS_TOKEN")
    if not token:
        print("No token found. Please register or set SPACETRADERS_TOKEN in .env")
        return

    # Initialize client and exploration manager
    client = SpaceTradersClient(token)
    explorer = ExplorationManager(client)
    
    # Get or purchase an explorer ship
    ship = explorer.get_explorer_ship()
    if not ship:
        print("Failed to get an explorer ship")
        return
        
    ship_symbol = ship["symbol"]
    print(f"Using explorer ship: {ship_symbol}")
    
    # Start exploring the current system
    print("\nStarting system exploration...")
    explorer.explore_system(ship_symbol)
    print("\nExploration complete!")
    
    # Print exploration summary
    print("\nExploration Summary:")
    print(f"Explored waypoints: {len(explorer.explored_waypoints)}")
    print(f"Charted waypoints: {len(explorer.charted_waypoints)}")


if __name__ == "__main__":
    main() 