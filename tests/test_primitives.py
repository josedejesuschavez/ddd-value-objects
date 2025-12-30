from src.ddd_value_objects.bool_value_object import BoolValueObject
from src.ddd_value_objects.float_value_object import FloatValueObject
from src.ddd_value_objects.int_value_object import IntValueObject
from src.ddd_value_objects.string_value_object import StringValueObject


def test_string_value_object():
    vo1 = StringValueObject("test")
    vo2 = StringValueObject("test")
    vo3 = StringValueObject("other")
    
    assert vo1.value == "test"
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert repr(vo1) == "StringValueObject(value='test')"

def test_int_value_object():
    vo1 = IntValueObject(10)
    vo2 = IntValueObject(10)
    vo3 = IntValueObject(20)
    
    assert vo1.value == 10
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert repr(vo1) == "IntValueObject(value=10)"

def test_float_value_object():
    vo1 = FloatValueObject(10.5)
    vo2 = FloatValueObject(10.5)
    vo3 = FloatValueObject(20.5)
    
    assert vo1.value == 10.5
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert repr(vo1) == "FloatValueObject(value=10.5)"

def test_bool_value_object():
    vo1 = BoolValueObject(True)
    vo2 = BoolValueObject(True)
    vo3 = BoolValueObject(False)
    
    assert vo1.value is True
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert repr(vo1) == "BoolValueObject(value=True)"
