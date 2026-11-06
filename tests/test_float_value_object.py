import pytest

from src.ddd_value_objects import FloatValueObject, InvalidArgumentError


def test_float_value_object_rejects_nan():
    with pytest.raises(InvalidArgumentError, match="Value must be finite"):
        FloatValueObject(float("nan"))


def test_float_value_object_rejects_infinity():
    with pytest.raises(InvalidArgumentError, match="Value must be finite"):
        FloatValueObject(float("inf"))


def test_float_value_object_rejects_negative_infinity():
    with pytest.raises(InvalidArgumentError, match="Value must be finite"):
        FloatValueObject(float("-inf"))


def test_float_value_object_accepts_finite_values():
    assert FloatValueObject(1.5).value == 1.5
    assert FloatValueObject(0.0).value == 0.0


def test_float_value_object_non_finite_error_message():
    vo = FloatValueObject(1.0)
    assert vo.get_non_finite_error_message(float("nan")) == "Value must be finite, got nan"


def test_float_value_object_error_message_templates():
    vo = FloatValueObject(1.0)
    assert vo.get_too_low_error_message_template() == "Value is less than minimum required {min_value}"
    assert vo.get_too_high_error_message_template() == "Value is greater than maximum allowed {max_value}"
