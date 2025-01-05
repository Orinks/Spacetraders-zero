from typing import Optional, Dict, Any

class SpaceTradersException(Exception):
	"""Base exception for SpaceTraders API errors."""
	pass

class SpaceTradersError(SpaceTradersException):
	"""Base exception for all SpaceTraders errors"""
	def __init__(self, message: str, response_data: Optional[Dict[str, Any]] = None):
		self.message = message
		self.response_data = response_data
		super().__init__(self.message)

class BadRequestError(SpaceTradersError):
    """Raised when the request is malformed or invalid (400)"""
    pass

class AuthenticationError(SpaceTradersError):
	"""Raised when there are authentication issues (401)"""
	pass

class RateLimitError(SpaceTradersError):
	"""Raised when hitting rate limits (429)"""
	def __init__(self, message: str, retry_after: int, response_data: Optional[Dict[str, Any]] = None):
		self.retry_after = retry_after
		super().__init__(message, response_data)

class ValidationError(SpaceTradersError):
	"""Raised when request validation fails (422)"""
	pass

class ResourceNotFoundError(SpaceTradersError):
	"""Raised when a requested resource is not found (404)"""
	pass

class ServerError(SpaceTradersError):
	"""Raised when the server encounters an error (500+)"""
	pass

class NetworkError(SpaceTradersError):
	"""Raised when there are network connectivity issues"""
	pass

class CooldownError(SpaceTradersError):
	"""Raised when an action cannot be performed due to cooldown"""
	def __init__(self, message: str, remaining_seconds: int, response_data: Optional[Dict[str, Any]] = None):
		self.remaining_seconds = remaining_seconds
		super().__init__(message, response_data)

class InsufficientResourcesError(SpaceTradersError):
    """Raised when there are insufficient resources to perform an action"""
    pass