import pytest
from unittest.mock import Mock, patch
import aiohttp
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.client import SpaceTradersClient
from src.exceptions import SpaceTradersError

@pytest.fixture
async def client():
	"""Create a test client instance."""
	return SpaceTradersClient("test_token")

@pytest.mark.asyncio
async def test_client_initialization(client):
	"""Test client initialization with token."""
	assert isinstance(client, SpaceTradersClient)
	assert client.token == "test_token"

@pytest.mark.asyncio
async def test_get_status(client):
	"""Test get_status method."""
	with patch('aiohttp.ClientSession.get') as mock_get:
		mock_response = Mock()
		mock_response.status = 200
		mock_response.json.return_value = {"status": "spacetraders is online"}
		mock_get.return_value.__aenter__.return_value = mock_response
		
		status = await client.get_status()
		assert status == {"status": "spacetraders is online"}

@pytest.mark.asyncio
async def test_get_status_error(client):
	"""Test get_status method with error response."""
	with patch('aiohttp.ClientSession.get') as mock_get:
		mock_response = Mock()
		mock_response.status = 500
		mock_get.return_value.__aenter__.return_value = mock_response
		
		with pytest.raises(SpaceTradersError):
			await client.get_status()