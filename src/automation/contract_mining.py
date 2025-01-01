import time
from typing import Any, Dict, List, Optional, Tuple

from client import ApiError, SpaceTradersClient

from .mining import (MiningError, mine_for_contract, mine_resources,
                     prepare_for_mining, wait_for_cooldown)


class ContractMiningError(Exception):
    """Custom exception for contract mining operations"""

    pass


def get_active_mining_contract(client: SpaceTradersClient) -> Optional[Dict[str, Any]]:
    """Find and accept a contract that requires resource delivery"""
    try:
        contracts = client.list_contracts()
        print("\nChecking available contracts...")

        # First, look for already accepted contracts
        accepted_contract = next(
            (
                contract
                for contract in contracts["data"]
                if (
                    not contract["fulfilled"]
                    and contract["accepted"]
                    and "deliver" in contract["terms"]
                    and len(contract["terms"]["deliver"]) > 0
                )
            ),
            None,
        )

        if accepted_contract:
            contract_details = client.get_contract(accepted_contract["id"])
            contract_data = contract_details["data"]
            print("\nFound accepted contract:")
            print(f"ID: {contract_data['id']}")
            print(f"Type: {contract_data['type']}")
            print("Deliverables:")
            for item in contract_data["terms"]["deliver"]:
                print(f"- {item['unitsRequired']} units of {item['tradeSymbol']}")
                print(f"  to {item['destinationSymbol']}")
            return contract_data

        # If no accepted contract, look for available contracts to accept
        available_contract = next(
            (
                contract
                for contract in contracts["data"]
                if (
                    not contract["fulfilled"]
                    and not contract["accepted"]
                    and "deliver" in contract["terms"]
                    and len(contract["terms"]["deliver"]) > 0
                )
            ),
            None,
        )

        if available_contract:
            print("\nFound available contract to accept:")
            print(f"ID: {available_contract['id']}")
            print(f"Type: {available_contract['type']}")
            print("Deliverables:")
            for item in available_contract["terms"]["deliver"]:
                print(f"- {item['unitsRequired']} units of {item['tradeSymbol']}")
                print(f"  to {item['destinationSymbol']}")

            # Accept the contract
            print("\nAccepting contract...")
            accept_result = client.accept_contract(available_contract["id"])
            print("Contract accepted!")

            # Get full contract details
            contract_details = client.get_contract(available_contract["id"])
            return contract_details["data"]

        print("\nNo suitable contracts found.")
        return None

    except ApiError as e:
        raise ContractMiningError(f"Failed to get contracts: {str(e)}")


def get_contract_resource_requirements(
    contract: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """Get resource requirements from contract"""
    try:
        if "terms" not in contract or "deliver" not in contract["terms"]:
            return []

        return [
            {
                "tradeSymbol": item["tradeSymbol"],
                "unitsRequired": item["unitsRequired"],
                "unitsDelivered": item.get("unitsFulfilled", 0),
                "destination": item["destinationSymbol"],
            }
            for item in contract["terms"]["deliver"]
        ]

    except Exception as e:
        raise ContractMiningError(f"Failed to get resource requirements: {str(e)}")


def find_mining_ship(client: SpaceTradersClient) -> Optional[str]:
    """Find a suitable mining ship or command the mining drone"""
    try:
        ships = client.list_ships()

        # First check if we have a command ship
        command_ship = next(
            (
                ship
                for ship in ships["data"]
                if ship["registration"]["role"] == "COMMAND"
                and not any(
                    mount["symbol"].startswith("MOUNT_MINING_LASER")
                    for mount in ship["mounts"]
                )
            ),
            None,
        )

        if command_ship:
            print(f"\nFound command ship: {command_ship['symbol']}")
            print(f"Location: {command_ship['nav']['waypointSymbol']}")
            print(f"Status: {command_ship['nav']['status']}")
            return command_ship["symbol"]

        # If no command ship, look for a mining ship directly
        mining_ship = next(
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

        if not mining_ship:
            print("No mining ships found.")
            return None

        print(f"\nSelected mining ship: {mining_ship['symbol']}")
        print(f"Location: {mining_ship['nav']['waypointSymbol']}")
        print(f"Status: {mining_ship['nav']['status']}")

        return mining_ship["symbol"]

    except ApiError as e:
        raise ContractMiningError(f"Failed to find mining ship: {str(e)}")


def handle_contract_mining(client: SpaceTradersClient) -> None:
    """Main function to handle contract mining operations"""
    try:
        print("\nLooking for contracts to work on...")

        # Find active mining contract
        contract = get_active_mining_contract(client)
        if not contract:
            print("No contracts available at the moment.")
            return

        # Find a suitable mining ship
        ship_symbol = find_mining_ship(client)
        if not ship_symbol:
            print("No mining ships available.")
            return

        print(f"\nWorking on contract: {contract['id']}")
        print(
            f"Payment on completion: {contract['terms']['payment']['onFulfilled']} credits"
        )
        if "onAccepted" in contract["terms"]["payment"]:
            print(
                f"Payment received for accepting: {contract['terms']['payment']['onAccepted']} credits"
            )

        # Get resource requirements
        requirements = get_contract_resource_requirements(contract)
        for req in requirements:
            print(f"\nResource requirement:")
            print(f"- Type: {req['tradeSymbol']}")
            print(f"- Needed: {req['unitsRequired']} units")
            print(f"- Delivered: {req['unitsDelivered']} units")
            print(f"- Remaining: {req['unitsRequired'] - req['unitsDelivered']} units")
            print(f"- Delivery location: {req['destination']}")

            # Mine if more resources needed
            if req["unitsRequired"] > req["unitsDelivered"]:
                units_needed = req["unitsRequired"] - req["unitsDelivered"]
                print(
                    f"\nStarting mining operation for {units_needed} units of {req['tradeSymbol']}"
                )

                try:
                    mining_results = mine_for_contract(
                        client,
                        ship_symbol,
                        contract["id"],
                        req["tradeSymbol"],
                        units_needed,
                        req["destination"],
                    )
                    print(f"Mining operation completed for {req['tradeSymbol']}")
                except Exception as e:
                    print(f"Contract mining failed: {str(e)}")
                    continue  # Try next requirement if this one fails

        # Check if contract is complete
        contract = client.get_contract(contract["id"])
        if all(
            item.get("unitsFulfilled", 0) >= item["unitsRequired"]
            for item in contract["data"]["terms"]["deliver"]
        ):
            print("\nAll deliveries complete. Fulfilling contract...")
            fulfill_result = client.fulfill_contract(contract["id"])
            payment = fulfill_result["data"]["contract"]["terms"]["payment"]
            print(f"Contract fulfilled! Received {payment['onFulfilled']} credits")

    except (ApiError, ContractMiningError, MiningError) as e:
        print(f"Contract mining failed: {str(e)}")
    except Exception as e:
        print(f"Unexpected error during contract mining: {str(e)}")
