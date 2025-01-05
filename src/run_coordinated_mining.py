import os

from src.automation.coordinated_mining import (CoordinatedMiningError,
                                           coordinate_mining)
from src.client import SpaceTradersClient


def main():
    """Run coordinated mining operation"""
    try:
        # Initialize client
        token = os.environ.get("SPACETRADERS_TOKEN")
        if not token:
            print("Error: SPACETRADERS_TOKEN environment variable not set")
            return

        client = SpaceTradersClient(token)

        # Get agent info for headquarters
        agent = client.get_agent()
        headquarters = agent["data"]["headquarters"]
        system = "-".join(headquarters.split("-")[:2])

        # Find a market to sell at (using headquarters for now)
        market_waypoint = headquarters

        print("\nStarting coordinated mining operation")
        print(f"System: {system}")
        print(f"Market: {market_waypoint}")

        # Start coordinated mining
        coordinate_mining(client, market_waypoint)

    except CoordinatedMiningError as e:
        print(f"\nCoordinated mining error: {str(e)}")
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")


if __name__ == "__main__":
    main()
