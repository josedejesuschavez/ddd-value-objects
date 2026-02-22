import pytest
from decimal import Decimal
from src.ddd_value_objects import DecimalValueObject, PositiveDecimalValueObject, InvalidArgumentError

def test_decimal_value_object_valid():
    val = Decimal("10.50")
    vo = DecimalValueObject(val)
    assert vo.value == val
    assert isinstance(vo.value, Decimal)

def test_decimal_value_object_equality():
    from src.ddd_value_objects import StringValueObject
    vo1 = DecimalValueObject(Decimal("10.50"))
    vo2 = DecimalValueObject(Decimal("10.50"))
    vo3 = DecimalValueObject(Decimal("10.51"))
    
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert not vo1.equals(StringValueObject("test"))

def test_positive_decimal_value_object_valid():
    val = Decimal("100.00")
    vo = PositiveDecimalValueObject(val)
    assert vo.value == val

def test_positive_decimal_value_object_zero():
    val = Decimal("0.00")
    vo = PositiveDecimalValueObject(val)
    assert vo.value == val

def test_positive_decimal_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a positive decimal"):
        PositiveDecimalValueObject(Decimal("-1.00"))

def test_decimal_value_object_repr():
    vo = DecimalValueObject(Decimal("10.5"))
    assert repr(vo) == "DecimalValueObject(value=Decimal('10.5'))"

def test_positive_decimal_value_object_repr():
    vo = PositiveDecimalValueObject(Decimal("20.0"))
    assert repr(vo) == "PositiveDecimalValueObject(value=Decimal('20.0'))"
