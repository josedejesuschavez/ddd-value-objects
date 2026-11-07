import pytest
from datetime import date, datetime, timedelta, timezone

from src.ddd_value_objects.date_time_value_object import DateTimeValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError


def test_date_time_value_object_stores_aware_datetime():
    dt = datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc)
    vo1 = DateTimeValueObject(dt)
    vo2 = DateTimeValueObject(dt)

    assert vo1.value == dt
    assert vo1.equals(vo2)
    assert hash(vo1) == hash(vo2)


def test_date_time_value_object_coerces_naive_to_utc():
    vo = DateTimeValueObject(datetime(2024, 1, 15, 10, 30))
    assert vo.value.tzinfo == timezone.utc
    assert vo.value == datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc)


def test_date_time_value_object_parses_iso_string():
    vo = DateTimeValueObject("2024-01-15T10:30:00+00:00")
    assert vo.value == datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc)


def test_date_time_value_object_parses_iso_string_with_z_suffix():
    vo = DateTimeValueObject("2024-01-15T10:30:00Z")
    assert vo.value == datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc)


def test_date_time_value_object_naive_iso_string_becomes_utc():
    # Coercion makes equivalent inputs equal: the canonical form is what
    # gets compared and hashed.
    vo_from_str = DateTimeValueObject("2024-01-15T10:30:00")
    vo_from_dt = DateTimeValueObject(datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc))
    assert vo_from_str == vo_from_dt
    assert hash(vo_from_str) == hash(vo_from_dt)


def test_date_time_value_object_strips_surrounding_whitespace():
    vo = DateTimeValueObject("  2024-01-15T10:30:00  ")
    assert vo.value == datetime(2024, 1, 15, 10, 30, tzinfo=timezone.utc)


def test_date_time_value_object_preserves_non_utc_offset():
    offset = timezone(timedelta(hours=-6))
    vo = DateTimeValueObject(datetime(2024, 1, 15, 10, 30, tzinfo=offset))
    assert vo.value.utcoffset() == timedelta(hours=-6)


def test_date_time_value_object_rejects_invalid_string():
    with pytest.raises(InvalidArgumentError, match="is not a valid ISO datetime"):
        DateTimeValueObject("15/01/2024 10:30")


def test_date_time_value_object_rejects_other_types():
    with pytest.raises(InvalidArgumentError, match="must be a datetime or ISO datetime string"):
        DateTimeValueObject(1698412200)


def test_date_time_value_object_rejects_plain_date():
    with pytest.raises(InvalidArgumentError, match="must be a datetime or ISO datetime string"):
        DateTimeValueObject(date(2024, 1, 15))
