import pytest
import logging
from src.permission_logger import PermissionLogger, UserPermissionLevel

class TestPermissionLogger:
    def test_default_initialization(self):
        """Test default logger initialization."""
        logger = PermissionLogger()
        assert logger._min_permission_level == UserPermissionLevel.USER
    
    def test_custom_initialization(self):
        """Test custom logger initialization."""
        logger = PermissionLogger(min_permission_level=UserPermissionLevel.ADMIN)
        assert logger._min_permission_level == UserPermissionLevel.ADMIN
    
    def test_successful_log_with_sufficient_permissions(self, caplog):
        """Test logging with sufficient permissions."""
        logger = PermissionLogger(min_permission_level=UserPermissionLevel.USER)
        caplog.set_level(logging.INFO)
        
        result = logger.log("Test message", user_permission=UserPermissionLevel.USER)
        assert result is True
        assert "Test message" in caplog.text
    
    def test_log_with_higher_permissions(self, caplog):
        """Test logging with higher than required permissions."""
        logger = PermissionLogger(min_permission_level=UserPermissionLevel.USER)
        caplog.set_level(logging.INFO)
        
        result = logger.log("Admin message", user_permission=UserPermissionLevel.ADMIN)
        assert result is True
        assert "Admin message" in caplog.text
    
    def test_log_with_insufficient_permissions(self, caplog):
        """Test logging with insufficient permissions."""
        logger = PermissionLogger(min_permission_level=UserPermissionLevel.ADMIN)
        caplog.set_level(logging.INFO)
        
        result = logger.log("Guest message", user_permission=UserPermissionLevel.GUEST)
        assert result is False
        assert "Guest message" not in caplog.text
    
    def test_log_with_default_permission(self, caplog):
        """Test logging with default permissions."""
        logger = PermissionLogger(min_permission_level=UserPermissionLevel.USER)
        caplog.set_level(logging.INFO)
        
        result = logger.log("Default message")
        assert result is True
        assert "Default message" in caplog.text
    
    def test_empty_message_raises_error(self):
        """Test that empty message raises ValueError."""
        logger = PermissionLogger()
        
        with pytest.raises(ValueError, match="Message cannot be empty"):
            logger.log("")
    
    def test_invalid_permission_type_raises_error(self):
        """Test that invalid permission type raises TypeError."""
        logger = PermissionLogger()
        
        with pytest.raises(TypeError, match="user_permission must be a UserPermissionLevel"):
            logger.log("Test message", user_permission="not a permission")
    
    def test_custom_log_level(self, caplog):
        """Test logging with a custom log level."""
        logger = PermissionLogger()
        caplog.set_level(logging.WARNING)
        
        result = logger.log("Warning message", level=logging.WARNING)
        assert result is True
        assert "Warning message" in caplog.text