import pytest
from datetime import datetime, date, timedelta
from src.date_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_strings():
    """Test calculating days between dates using string inputs"""
    assert calculate_days_between_dates("2023-01-01", "2023-01-10") == 9
    assert calculate_days_between_dates("2023-01-10", "2023-01-01") == 9

def test_calculate_days_between_dates_date_objects():
    """Test calculating days between dates using date objects"""
    date1 = date(2023, 1, 1)
    date2 = date(2023, 1, 10)
    assert calculate_days_between_dates(date1, date2) == 9

def test_calculate_days_between_dates_datetime_objects():
    """Test calculating days between dates using datetime objects"""
    datetime1 = datetime(2023, 1, 1, 12, 0)
    datetime2 = datetime(2023, 1, 10, 14, 30)
    assert calculate_days_between_dates(datetime1, datetime2) == 9

def test_same_date():
    """Test when both dates are the same"""
    assert calculate_days_between_dates("2023-01-01", "2023-01-01") == 0

def test_dates_across_years():
    """Test calculating days between dates in different years"""
    assert calculate_days_between_dates("2022-12-31", "2023-01-01") == 1
    assert calculate_days_between_dates("2019-12-31", "2020-01-01") == 1

def test_invalid_date_format():
    """Test handling of invalid date formats"""
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates("01-01-2023", "2023-01-10")
    
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates("2023-01-10", "10-01-2023")

def test_order_independence():
    """Test that order of dates doesn't matter"""
    assert calculate_days_between_dates("2023-01-01", "2023-01-10") == \
           calculate_days_between_dates("2023-01-10", "2023-01-01")