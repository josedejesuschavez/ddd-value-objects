import pytest
from decimal import Decimal

from src.ddd_value_objects import (
    NonNegativeIntValueObject,
    NonNegativeFloatValueObject,
    NonNegativeDecimalValueObject,
    InvalidArgumentError,
)


def test_non_negative_int_value_object():
    vo1 = NonNegativeIntValueObject(10)
    vo2 = NonNegativeIntValueObject(10)
    vo3 = NonNegativeIntValueObject(20)

    assert vo1.value == 10
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert repr(vo1) == "NonNegativeIntValueObject(value=10)"


def test_non_negative_int_value_object_zero():
    vo = NonNegativeIntValueObject(0)
    assert vo.value == 0


def test_non_negative_int_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a non-negative integer"):
        NonNegativeIntValueObject(-1)


def test_non_negative_float_value_object():
    vo1 = NonNegativeFloatValueObject(10.5)
    vo2 = NonNegativeFloatValueObject(10.5)
    vo3 = NonNegativeFloatValueObject(20.5)

    assert vo1.value == 10.5
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert repr(vo1) == "NonNegativeFloatValueObject(value=10.5)"


def test_non_negative_float_value_object_zero():
    vo = NonNegativeFloatValueObject(0.0)
    assert vo.value == 0.0


def test_non_negative_float_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a non-negative float"):
        NonNegativeFloatValueObject(-1.5)


def test_non_negative_decimal_value_object():
    vo1 = NonNegativeDecimalValueObject(Decimal("10.5"))
    assert vo1.value == Decimal("10.5")


def test_non_negative_decimal_value_object_zero():
    vo = NonNegativeDecimalValueObject(Decimal("0"))
    assert vo.value == Decimal("0")


def test_non_negative_decimal_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a non-negative decimal"):
        NonNegativeDecimalValueObject(Decimal("-1.5"))


def test_non_negative_int_with_extra_range():
    class PortNumber(NonNegativeIntValueObject):
        def max_value(self) -> int:
            return 65535

    assert PortNumber(8080).value == 8080
    with pytest.raises(InvalidArgumentError, match="greater than maximum allowed 65535"):
        PortNumber(70000)
    with pytest.raises(InvalidArgumentError, match="is not a non-negative integer"):
        PortNumber(-1)
