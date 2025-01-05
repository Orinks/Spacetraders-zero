import os
import time
from typing import Optional

from dotenv import load_dotenv

from src.automation.goals import GoalManager
from src.client import (
    SpaceTradersClient,
    SpaceTradersError,
    ValidationError,
    AuthenticationError,
    NetworkError,
)


def main():
    """Main entry point"""
    load_dotenv()
    token = os.getenv("SPACETRADERS_TOKEN")

    if not token:
        try:
            # Register new agent if no token exists
            symbol = input("Enter agent symbol (3-14 characters, A-Z, 0-9, -): ")
            faction = input("Enter faction (default: COSMIC): ") or "COSMIC"
            
            result = SpaceTradersClient.register_new_agent(symbol, faction)
            token = result["data"]["token"]
            agent_info = result["data"]["agent"]
            print(f"\nRegistration successful!")
            print(f"Token saved to .env file")
            
        except ValidationError as e:
            print(f"Registration failed: Invalid input - {str(e)}")
            return
        except NetworkError as e:
            print(f"Registration failed: Network error - {str(e)}")
            return
        except SpaceTradersError as e:
            print(f"Registration failed: {str(e)}")
            return

    try:
        # Initialize client with token
        client = SpaceTradersClient(token)
        
        # Get agent info
        agent_info = client.get_agent()["data"]
        print(f"\nAgent: {agent_info['symbol']}")
        print(f"Credits: {agent_info['credits']}")
        print(f"Headquarters: {agent_info['headquarters']}")

        print("\nInitializing autonomous agent...")
        goal_manager = GoalManager(client)
        
        print("Agent is now running autonomously. Press Ctrl+C to stop.")
        try:
            while True:
                goal_manager.update()
                time.sleep(5)  # Small delay between updates
                
        except KeyboardInterrupt:
            print("\nGracefully shutting down...")
        except Exception as e:
            print(f"\nUnexpected error: {str(e)}")
        finally:
            print("\nAgent stopped.")
            
    except AuthenticationError:
        print("Invalid token. Please check your SPACETRADERS_TOKEN in .env")
    except NetworkError as e:
        print(f"Network error: {str(e)}")
    except SpaceTradersError as e:
        print(f"Failed to get agent info: {str(e)}")


if __name__ == "__main__":
    main()

