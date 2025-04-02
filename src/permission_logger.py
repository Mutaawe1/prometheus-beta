import logging
from enum import Enum
from typing import Optional, Union

class UserPermissionLevel(Enum):
    """Enum representing different user permission levels."""
    GUEST = 1
    USER = 2
    ADMIN = 3

class PermissionLogger:
    """
    A logger that controls message logging based on user permission levels.
    
    The logger allows logging messages only if the user's permission level 
    meets or exceeds the specified log level.
    """
    
    def __init__(self, min_permission_level: UserPermissionLevel = UserPermissionLevel.USER):
        """
        Initialize the PermissionLogger.
        
        Args:
            min_permission_level (UserPermissionLevel, optional): 
                Minimum permission level required to log messages. 
                Defaults to UserPermissionLevel.USER.
        """
        self._min_permission_level = min_permission_level
        self._logger = logging.getLogger(__name__)
        
        # Configure basic logging if not already configured
        if not self._logger.handlers:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s'
            )
    
    def log(self, 
            message: str, 
            user_permission: Optional[UserPermissionLevel] = None, 
            level: int = logging.INFO
    ) -> bool:
        """
        Log a message based on user permissions.
        
        Args:
            message (str): The message to log
            user_permission (Optional[UserPermissionLevel], optional): 
                User's permission level. If None, uses the logger's default.
            level (int, optional): Logging level. Defaults to logging.INFO.
        
        Returns:
            bool: True if message was logged, False otherwise
        
        Raises:
            ValueError: If message is empty
            TypeError: If user_permission is not a UserPermissionLevel
        """
        # Validate input
        if not message:
            raise ValueError("Message cannot be empty")
        
        # Use default min permission if not specified
        if user_permission is None:
            user_permission = self._min_permission_level
        
        # Validate user permission
        if not isinstance(user_permission, UserPermissionLevel):
            raise TypeError("user_permission must be a UserPermissionLevel")
        
        # Check if user has sufficient permissions to log
        if user_permission.value >= self._min_permission_level.value:
            # Log the message
            self._logger.log(level, message)
            return True
        
        return False