import pytest
from datetime import date, datetime, timezone

from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError
from src.ddd_value_objects.value_object import ValueObject


class MockValueObject(ValueObject[int]):
    def equals(self, other: ValueObject) -> bool:
        return super().equals(other)

def test_value_object_stores_value():
    value = 10
    vo = MockValueObject(value)
    assert vo.value == value

def test_value_object_to_string():
    value = 10
    vo = MockValueObject(value)
    assert str(vo) == str(value)

def test_value_object_raises_error_if_none():
    with pytest.raises(InvalidArgumentError, match="Value must be defined"):
        MockValueObject(None)

def test_value_object_equality():
    vo1 = MockValueObject(10)
    vo2 = MockValueObject(10)
    vo3 = MockValueObject(20)
    
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    
    assert vo1 == vo2
    assert vo1 != vo3
    assert vo1 != "not a value object"
    assert vo1 != None

def test_value_object_hash():
    vo1 = MockValueObject(10)
    vo2 = MockValueObject(10)
    vo3 = MockValueObject(20)
    
    assert hash(vo1) == hash(vo2)
    assert hash(vo1) != hash(vo3)

def test_value_object_supports_date_and_datetime():
    # date/datetime joined the ValueType constraint because both are
    # immutable and hashable, so they satisfy the wrapper contract as-is.
    class MockDateValueObject(ValueObject[date]):
        pass

    class MockDateTimeValueObject(ValueObject[datetime]):
        pass

    vo_date = MockDateValueObject(date(2024, 1, 15))
    vo_datetime = MockDateTimeValueObject(datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc))

    assert vo_date.value == date(2024, 1, 15)
    assert vo_datetime.value == datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc)
    assert vo_date == MockDateValueObject(date(2024, 1, 15))
    assert hash(vo_date) == hash(MockDateValueObject(date(2024, 1, 15)))


def test_invalid_argument_error_str_repr():
    err = InvalidArgumentError("Test message", {"param": "value"})
    assert str(err) == "Test message {'param': 'value'}"
    assert repr(err) == "InvalidArgumentError(message='Test message', params={'param': 'value'})"
