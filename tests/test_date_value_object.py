import pytest
from src.ddd_value_objects.date_value_object import DateValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError

def test_date_value_object():
    ts = 1698364800
    vo1 = DateValueObject(ts)
    vo2 = DateValueObject(ts)
    vo3 = DateValueObject(1698451200)
    
    assert vo1.value == ts
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert repr(vo1) == f"DateValueObject(value={ts})"

def test_date_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a valid Unix timestamp"):
        DateValueObject(99999999999999)

def test_date_value_object_comparison():
    past_ts = 1000000000
    future_ts = 2000000000
    vo_past = DateValueObject(past_ts)
    vo_future = DateValueObject(future_ts)
    
    assert vo_past.value < vo_future.value
