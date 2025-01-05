"""Automation package for SpaceTraders client."""

from .mining_manager import MiningManager, MiningTarget
from .exploration import ExplorationManager
from .coordinated_mining import coordinate_mining, CoordinatedMiningError
from .contract_mining import handle_contract_mining
from .ship_utils import find_nearest_shipyard
from .ship_buyer import find_and_purchase_ship
from .goals import GoalManager

__all__ = [
    'MiningManager',
    'MiningTarget',
    'ExplorationManager',
    'coordinate_mining',
    'CoordinatedMiningError',
    'handle_contract_mining',
    'find_nearest_shipyard',
    'find_and_purchase_ship',
    'GoalManager',
]
