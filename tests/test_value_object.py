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

def test_value_object_immutability():
    vo = MockValueObject(10)
    with pytest.raises(TypeError, match="MockValueObject is immutable"):
        vo.value = 20
    with pytest.raises(TypeError, match="MockValueObject is immutable"):
        del vo._value

def test_value_object_not_initialized():
    class UninitializedVO(ValueObject[int]):
        def __init__(self, value: int):
            # No llama a super().__init__(value)
            pass
        def equals(self, other: ValueObject) -> bool:
            return True
            
    vo = UninitializedVO(10)
    vo.any_attr = 100
    assert vo.any_attr == 100
    del vo.any_attr

def test_invalid_argument_error_str_repr():
    err = InvalidArgumentError("Test message", {"param": "value"})
    assert str(err) == "Test message {'param': 'value'}"
    assert repr(err) == "InvalidArgumentError(message='Test message', params={'param': 'value'})"
