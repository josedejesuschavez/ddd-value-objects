import pytest

from src.ddd_value_objects.date_time_value_object import DateTimeValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError


def test_date_time_value_object():
    ts = 1698412200
    vo1 = DateTimeValueObject(ts)
    vo2 = DateTimeValueObject(ts)
    vo3 = DateTimeValueObject(1698412201)
    
    assert vo1.value == ts
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert repr(vo1) == f"DateTimeValueObject(value={ts})"

def test_date_time_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a valid Unix timestamp"):
        DateTimeValueObject(99999999999999)

def test_date_time_value_object_comparison():
    past_ts = 1000000000
    future_ts = 2000000000
    vo_past = DateTimeValueObject(past_ts)
    vo_future = DateTimeValueObject(future_ts)
    
    assert vo_past.value < vo_future.value
