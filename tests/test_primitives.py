from decimal import Decimal

import pytest

from ddd_value_objects import (
    DecimalValueObject,
    BoolValueObject,
    FloatValueObject,
    IntValueObject,
    StringValueObject,
    InvalidArgumentError,
    PositiveDecimalValueObject,
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

def test_custom_error_message():
    class FirstName(StringValueObject):
        def get_invalid_type_error_message(self, value):
            return f"Custom error for {value}"
    
    with pytest.raises(InvalidArgumentError, match=r"Custom error for 123"):
        FirstName(123)

def test_float_value_object_custom_too_high_message():
    class CustomMessageFloat(FloatValueObject):
        def max_value(self) -> float:
            return 10.0
        def get_too_high_error_message(self, value, max_val):
            return f'Too high: {value} > {max_val}'

    with pytest.raises(InvalidArgumentError, match='Too high: 15.0 > 10.0'):
        CustomMessageFloat(15.0)

def test_float_value_object_custom_too_low_message():
    class CustomMessageFloatLow(FloatValueObject):
        def min_value(self) -> float:
            return 10.0
        def get_too_low_error_message(self, value, min_val):
            return f'Too low: {value} < {min_val}'

    with pytest.raises(InvalidArgumentError, match='Too low: 5.0 < 10.0'):
        CustomMessageFloatLow(5.0)

def test_float_value_object_default_too_low_message():
    class RestrictedFloatLow(FloatValueObject):
        def min_value(self) -> float:
            return 10.0

    with pytest.raises(InvalidArgumentError, match='Value 5.0 is less than minimum required 10.0'):
        RestrictedFloatLow(5.0)


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


def test_decimal_value_object_max_value():
    class RestrictedDecimal(DecimalValueObject):
        def max_value(self) -> Decimal:
            return Decimal('100.0')

    assert RestrictedDecimal(Decimal('50.0')).value == Decimal('50.0')
    with pytest.raises(InvalidArgumentError, match='greater than maximum allowed 100.0'):
        RestrictedDecimal(Decimal('150.0'))


def test_decimal_value_object_min_value():
    class RestrictedDecimalMin(DecimalValueObject):
        def min_value(self) -> Decimal:
            return Decimal('10.0')

    assert RestrictedDecimalMin(Decimal('15.0')).value == Decimal('15.0')
    with pytest.raises(InvalidArgumentError, match='less than minimum required 10.0'):
        RestrictedDecimalMin(Decimal('5.0'))


def test_decimal_value_object_custom_too_high_message():
    class CustomMessageDecimal(DecimalValueObject):
        def max_value(self) -> Decimal:
            return Decimal('10.0')

        def get_too_high_error_message(self, value, max_val):
            return f'Too high: {value} > {max_val}'

    with pytest.raises(InvalidArgumentError, match='Too high: 15.0 > 10.0'):
        CustomMessageDecimal(Decimal('15.0'))
