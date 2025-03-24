import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_datetime():
    """Test adding days to a datetime object."""
    base_date = datetime(2023, 1, 15)
    result = add_days_to_date(base_date, 10)
    assert result == datetime(2023, 1, 25)

def test_add_days_to_date_string():
    """Test adding days to a date string."""
    base_date = "2023-01-15"
    result = add_days_to_date(base_date, 10)
    assert result == datetime(2023, 1, 25)

def test_subtract_days():
    """Test subtracting days."""
    base_date = datetime(2023, 1, 15)
    result = add_days_to_date(base_date, -5)
    assert result == datetime(2023, 1, 10)

def test_add_zero_days():
    """Test adding zero days."""
    base_date = datetime(2023, 1, 15)
    result = add_days_to_date(base_date, 0)
    assert result == base_date

def test_large_day_count():
    """Test adding a large number of days."""
    base_date = datetime(2023, 1, 15)
    result = add_days_to_date(base_date, 365)
    assert result == datetime(2024, 1, 15)

def test_invalid_date_type():
    """Test that invalid date type raises TypeError."""
    with pytest.raises(TypeError):
        add_days_to_date(123, 5)

def test_invalid_days_type():
    """Test that invalid days type raises ValueError."""
    base_date = datetime(2023, 1, 15)
    with pytest.raises(ValueError):
        add_days_to_date(base_date, "5")

def test_invalid_date_string():
    """Test that invalid date string raises TypeError."""
    with pytest.raises(TypeError):
        add_days_to_date("2023/01/15", 5)