from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from enum import Enum, auto
import time

from src.client import SpaceTradersClient
from .mining_manager import MiningManager, MiningTarget
from .ship_utils import find_nearest_shipyard, purchase_mining_drone


class GoalPriority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


@dataclass
class Goal:
    name: str
    priority: GoalPriority
    prerequisites: List[str]
    completion_criteria: Dict[str, Any]
    timeout: Optional[float] = None
    started_at: Optional[float] = None
    completed_at: Optional[float] = None

    def is_expired(self) -> bool:
        if not self.timeout or not self.started_at:
            return False
        return time.time() - self.started_at > self.timeout

    def start(self):
        self.started_at = time.time()

    def complete(self):
        self.completed_at = time.time()


class GoalManager:
    def __init__(self, client: SpaceTradersClient):
        self.client = client
        self.active_goals: List[Goal] = []
        self.completed_goals: List[Goal] = []
        self.failed_goals: List[Goal] = []
        self.mining_mgr = MiningManager(client)

    def evaluate_agent_state(self) -> Dict[str, Any]:
        """Evaluate current agent state to inform goal selection"""
        state = {
            "credits": 0,
            "ships": [],
            "has_mining_ships": False,
            "has_active_contract": False,
            "contract_id": None,
            "current_system": None
        }
        
        try:
            agent = self.client.get_agent()
            state["credits"] = agent["data"]["credits"]
            state["current_system"] = "-".join(agent["data"]["headquarters"].split("-")[:2])
            
            ships = self.client.list_ships()
            state["ships"] = ships["data"]
            
            # Initialize mining manager if needed
            if not self.mining_mgr.mining_drone:
                self.mining_mgr.initialize_mining_ships()
            
            # Check if we have mining capability
            state["has_mining_ships"] = bool(self.mining_mgr.mining_drone)
            
            contracts = self.client.list_contracts()
            active_contracts = [c for c in contracts["data"] if c["accepted"] and not c["fulfilled"]]
            state["has_active_contract"] = bool(active_contracts)
            if active_contracts:
                state["contract_id"] = active_contracts[0]["id"]
                
        except Exception as e:
            print(f"Error evaluating agent state: {str(e)}")
            
        return state

    def generate_goals(self, state: Dict[str, Any]) -> List[Goal]:
        """Generate appropriate goals based on current state"""
        goals = []
        
        # If we don't have mining ships, that's our top priority
        if not state["has_mining_ships"]:
            goals.append(Goal(
                name="acquire_mining_ships",
                priority=GoalPriority.CRITICAL,
                prerequisites=[],
                completion_criteria={"has_mining_ships": True},
                timeout=3600  # 1 hour timeout
            ))
            return goals  # Return early as we need ships first
            
        # If we have no active contract, get one
        if not state["has_active_contract"]:
            goals.append(Goal(
                name="acquire_contract",
                priority=GoalPriority.HIGH,
                prerequisites=["has_mining_ships"],
                completion_criteria={"has_active_contract": True},
                timeout=600  # 10 minute timeout
            ))
            
        # If we have both ships and contract, mine!
        if state["has_mining_ships"] and state["has_active_contract"]:
            goals.append(Goal(
                name="fulfill_contract",
                priority=GoalPriority.MEDIUM,
                prerequisites=["has_mining_ships", "has_active_contract"],
                completion_criteria={"contract_fulfilled": True},
                timeout=7200  # 2 hour timeout
            ))
            
        return goals

    def execute_goal(self, goal: Goal, state: Dict[str, Any]) -> bool:
        """Execute a specific goal and return success status"""
        if goal.name == "acquire_mining_ships":
            try:
                print("Searching for nearest shipyard...")
                # Find nearest shipyard
                shipyard = find_nearest_shipyard(self.client, state["current_system"])
                if not shipyard:
                    print("No shipyard found in nearby systems")
                    return False
                    
                print(f"Found shipyard at {shipyard['symbol']}, attempting to purchase mining drone...")
                # Try to purchase mining drone
                success = purchase_mining_drone(self.client, shipyard["symbol"])
                if success:
                    print("Successfully purchased mining drone")
                    # Reinitialize mining manager with new ships
                    self.mining_mgr.initialize_mining_ships()
                return success
                
            except Exception as e:
                print(f"Error acquiring mining ships: {str(e)}")
                return False
            
        elif goal.name == "acquire_contract":
            try:
                print("Searching for available contracts...")
                contracts = self.client.list_contracts()
                for contract in contracts["data"]:
                    if not contract["accepted"]:
                        print(f"Found contract {contract['id']}, attempting to accept...")
                        self.client.accept_contract(contract["id"])
                        return True
                print("No available contracts found")
                return False
            except Exception as e:
                print(f"Error acquiring contract: {str(e)}")
                return False
                
        elif goal.name == "fulfill_contract":
            try:
                if state["contract_id"]:
                    # Get contract details
                    print(f"Getting details for contract {state['contract_id']}...")
                    contract = self.client.get_contract(state["contract_id"])
                    if contract["data"]["fulfilled"]:
                        print("Contract already fulfilled")
                        return True
                        
                    print("Setting up mining operation for contract fulfillment...")
                    # Create mining target for contract
                    target = MiningTarget(
                        waypoint_symbol="",  # Will be determined by mining manager
                        resource_type=None,  # Will mine any resource needed by contract
                        units_required=None  # Will mine until contract is fulfilled
                    )
                    
                    print("Starting mining operation...")
                    # Start mining operation
                    self.mining_mgr.mine_resources(target, state["contract_id"])
                    return True
                    
            except Exception as e:
                print(f"Error fulfilling contract: {str(e)}")
                return False
                
        return False

    def update(self) -> None:
        """Main update loop for goal management"""
        # Evaluate current state
        state = self.evaluate_agent_state()
        
        # Remove expired goals
        self.active_goals = [g for g in self.active_goals if not g.is_expired()]
        
        # Generate new goals if needed
        if not self.active_goals:
            self.active_goals.extend(self.generate_goals(state))
        
        # Sort goals by priority
        self.active_goals.sort(key=lambda g: g.priority.value, reverse=True)
        
        # Execute highest priority goal
        if self.active_goals:
            current_goal = self.active_goals[0]
            if not current_goal.started_at:
                current_goal.start()
                print(f"\nStarting goal: {current_goal.name}")
                
            success = self.execute_goal(current_goal, state)
            
            if success:
                current_goal.complete()
                print(f"Completed goal: {current_goal.name}")
                self.completed_goals.append(current_goal)
                self.active_goals.pop(0)
            elif current_goal.is_expired():
                print(f"Goal expired: {current_goal.name}")
                self.failed_goals.append(current_goal)
                self.active_goals.pop(0) 