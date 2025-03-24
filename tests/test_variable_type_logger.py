import pytest
import logging
from src.variable_type_logger import log_variable_type

def test_log_variable_type(caplog):
    """
    Test logging of different variable types.
    """
    # Test logging of integer
    caplog.set_level(logging.INFO)
    result = log_variable_type(42)
    assert result == 'int'
    assert "Variable type: int" in caplog.text

    # Clear the log for the next test
    caplog.clear()

    # Test logging of string
    result = log_variable_type("Hello")
    assert result == 'str'
    assert "Variable type: str" in caplog.text

    # Clear the log for the next test
    caplog.clear()

    # Test logging of list
    result = log_variable_type([1, 2, 3])
    assert result == 'list'
    assert "Variable type: list" in caplog.text

    # Clear the log for the next test
    caplog.clear()

    # Test logging of dictionary
    result = log_variable_type({"key": "value"})
    assert result == 'dict'
    assert "Variable type: dict" in caplog.text

def test_log_variable_type_with_none(caplog):
    """
    Test logging of None type.
    """
    caplog.set_level(logging.INFO)
    result = log_variable_type(None)
    assert result == 'NoneType'
    assert "Variable type: NoneType" in caplog.text

def test_log_variable_type_with_custom_class(caplog):
    """
    Test logging of a custom class type.
    """
    class TestClass:
        pass

    test_instance = TestClass()
    caplog.set_level(logging.INFO)
    result = log_variable_type(test_instance)
    assert result == 'TestClass'
    assert "Variable type: TestClass" in caplog.text