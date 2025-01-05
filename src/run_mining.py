import os
import asyncio
import logging
from dotenv import load_dotenv

from src.client import SpaceTradersClient
from src.automation.mining_manager import MiningManager, MiningTarget

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def main():
    """Run mining operation with automatic coordination"""
    try:
        # Load environment variables
        load_dotenv()
        token = os.getenv("SPACETRADERS_TOKEN")
        if not token:
            logger.error("No token found. Please register or set SPACETRADERS_TOKEN in .env")
            return

        # Initialize client and mining manager
        client = SpaceTradersClient(token)
        mining_mgr = MiningManager(client)
        
        # Initialize mining ships
        if not mining_mgr.initialize_mining_ships():
            logger.error("Failed to initialize mining ships")
            return
            
        # Get initial mining status
        status = mining_mgr.get_mining_status()
        logger.info("\nMining Configuration:")
        logger.info(f"Mode: {status['mode']}")
        for ship_type, ship_info in status["ships"].items():
            logger.info(f"\n{ship_type.title()} Ship:")
            logger.info(f"Symbol: {ship_info.symbol}")
            logger.info(f"Location: {ship_info.nav.waypoint_symbol}")
            logger.info(f"Status: {ship_info.nav.status}")
            logger.info(f"Cargo: {ship_info.cargo.units}/{ship_info.cargo.capacity}")
        
        # Start mining operation
        logger.info("\nStarting mining operation...")
        target = MiningTarget(
            waypoint_symbol="",  # Will be determined by mining manager
            resource_type=None,  # Mine any resource
            units_required=None  # Mine until full
        )
        await mining_mgr.mine_resources(target)
        
        # Get final status
        final_status = mining_mgr.get_mining_status()
        logger.info("\nMining Operation Complete!")
        logger.info("\nFinal Status:")
        for ship_type, ship_info in final_status["ships"].items():
            logger.info(f"\n{ship_type.title()} Ship:")
            logger.info(f"Location: {ship_info.nav.waypoint_symbol}")
            logger.info(f"Cargo: {ship_info.cargo.units}/{ship_info.cargo.capacity}")

    except Exception as e:
        logger.error(f"\nUnexpected error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main()) 