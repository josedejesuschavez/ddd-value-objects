import pytest

from src.ddd_value_objects.positive_float_value_object import PositiveFloatValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError


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
