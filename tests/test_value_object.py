import pytest

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
