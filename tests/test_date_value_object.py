import pytest
from datetime import date, datetime

from src.ddd_value_objects.date_value_object import DateValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError


def test_date_value_object_stores_date():
    d = date(2024, 1, 15)
    vo1 = DateValueObject(d)
    vo2 = DateValueObject(d)

    assert vo1.value == d
    assert vo1.equals(vo2)
    assert hash(vo1) == hash(vo2)
    assert repr(vo1) == "DateValueObject(value=datetime.date(2024, 1, 15))"


def test_date_value_object_parses_iso_string():
    vo = DateValueObject("2024-01-15")
    assert vo.value == date(2024, 1, 15)
    assert vo == DateValueObject(date(2024, 1, 15))


def test_date_value_object_strips_surrounding_whitespace():
    vo = DateValueObject("  2024-01-15  ")
    assert vo.value == date(2024, 1, 15)


def test_date_value_object_rejects_invalid_string():
    with pytest.raises(InvalidArgumentError, match="is not a valid ISO date"):
        DateValueObject("15/01/2024")


def test_date_value_object_rejects_datetime():
    # datetime subclasses date, but silently dropping the time component
    # would hide information.
    with pytest.raises(InvalidArgumentError, match="must be a date or ISO date string"):
        DateValueObject(datetime(2024, 1, 15, 10, 30))


def test_date_value_object_rejects_other_types():
    with pytest.raises(InvalidArgumentError, match="must be a date or ISO date string"):
        DateValueObject(1698364800)
