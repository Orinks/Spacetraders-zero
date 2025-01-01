import json
import time

from src.client import ApiError, SpaceTradersClient


def print_response(response):
    print(json.dumps(response, indent=2))


try:
    client = SpaceTradersClient()
    ship_symbol = "TRADER-BOT-001-1"
    target = "X1-MY38-ZB5Z"

    # Put ship in orbit
    print("\nPutting ship in orbit...")
    orbit_result = client.orbit_ship(ship_symbol)
    print("Orbit response:")
    print_response(orbit_result)

    # Wait a moment for status to update
    time.sleep(1)

    # Set flight mode to CRUISE
    print("\nSetting flight mode to CRUISE...")
    nav_update = client._make_request(
        "PATCH", f"my/ships/{ship_symbol}/nav", {"flightMode": "CRUISE"}
    )
    print("Flight mode response:")
    print_response(nav_update)

    # Wait a moment for status to update
    time.sleep(1)

    # Navigate to asteroid
    print(f"\nNavigating to {target}...")
    nav_result = client.navigate_ship(ship_symbol, target)
    print("Navigation response:")
    print_response(nav_result)

except ApiError as e:
    print(f"\nAPI Error: {str(e)}")
    try:
        error_data = json.loads(str(e))
        print("Error details:")
        print_response(error_data)
    except:
        pass
except Exception as e:
    print(f"\nUnexpected error: {str(e)}")
