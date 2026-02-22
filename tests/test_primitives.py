import pytest

from ddd_value_objects import (
    DecimalValueObject,
    BoolValueObject,
    FloatValueObject,
    IntValueObject,
    StringValueObject,
    InvalidArgumentError,
)


def test_string_value_object():
    vo1 = StringValueObject("test")
    vo2 = StringValueObject("test")
    vo3 = StringValueObject("other")
    
    assert vo1.value == "test"
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert not vo1.equals(IntValueObject(1))
    assert repr(vo1) == "StringValueObject(value='test')"

def test_int_value_object():
    vo1 = IntValueObject(10)
    vo2 = IntValueObject(10)
    vo3 = IntValueObject(20)
    
    assert vo1.value == 10
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert not vo1.equals(StringValueObject("10"))
    assert repr(vo1) == "IntValueObject(value=10)"

def test_float_value_object():
    vo1 = FloatValueObject(10.5)
    vo2 = FloatValueObject(10.5)
    vo3 = FloatValueObject(20.5)
    
    assert vo1.value == 10.5
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert not vo1.equals(IntValueObject(10))
    assert repr(vo1) == "FloatValueObject(value=10.5)"

def test_bool_value_object():
    vo1 = BoolValueObject(True)
    vo2 = BoolValueObject(True)
    vo3 = BoolValueObject(False)
    vo4 = StringValueObject("True")
    
    assert vo1.value is True
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert not vo1.equals(vo4)
    assert repr(vo1) == "BoolValueObject(value=True)"

def test_string_value_object_invalid_type():
    with pytest.raises(InvalidArgumentError, match=r"Value must be a string"):
        StringValueObject(123)

def test_int_value_object_invalid_type():
    with pytest.raises(InvalidArgumentError, match=r"Value must be a integer"):
        IntValueObject('10')

def test_float_value_object_invalid_type():
    with pytest.raises(InvalidArgumentError, match=r"Value must be a float"):
        FloatValueObject(10)

def test_bool_value_object_invalid_type():
    with pytest.raises(InvalidArgumentError, match=r"Value must be a boolean"):
        BoolValueObject(1)

def test_decimal_value_object_invalid_type():
    with pytest.raises(InvalidArgumentError, match=r"Value must be a decimal"):
        DecimalValueObject(10.5)
