import pytest
from src.ddd_value_objects import PositiveIntValueObject, PositiveFloatValueObject, InvalidArgumentError

def test_positive_int_value_object():
    vo1 = PositiveIntValueObject(10)
    vo2 = PositiveIntValueObject(10)
    vo3 = PositiveIntValueObject(20)
    
    assert vo1.value == 10
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert repr(vo1) == "PositiveIntValueObject(value=10)"

def test_positive_int_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a positive integer"):
        PositiveIntValueObject(-1)

def test_positive_int_value_object_zero():
    vo = PositiveIntValueObject(0)
    assert vo.value == 0

def test_positive_float_value_object():
    vo1 = PositiveFloatValueObject(10.5)
    vo2 = PositiveFloatValueObject(10.5)
    vo3 = PositiveFloatValueObject(20.5)
    
    assert vo1.value == 10.5
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert repr(vo1) == "PositiveFloatValueObject(value=10.5)"

def test_positive_float_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a positive float"):
        PositiveFloatValueObject(-1.5)

def test_positive_float_value_object_zero():
    vo = PositiveFloatValueObject(0.0)
    assert vo.value == 0.0
