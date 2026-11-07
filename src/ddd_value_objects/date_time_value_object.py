from dataclasses import dataclass
from datetime import datetime, timezone

from .value_object import ValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class DateTimeValueObject(ValueObject[datetime]):
    """Wraps a timezone-aware ``datetime``.

    Naive datetimes are coerced to UTC on construction to avoid the
    silent tz-confusion that bites multi-tenant apps. ISO strings are
    accepted and coerced the same way, so
    ``DateTimeValueObject("2024-01-15T10:30:00")`` equals
    ``DateTimeValueObject(datetime(2024, 1, 15, 10, 30, tzinfo=UTC))``.
    """

    def __init__(self, value: datetime | str):
        super().__init__(self._parse(value))

    def _parse(self, value: datetime | str) -> datetime:
        if isinstance(value, str):
            try:
                # datetime.fromisoformat only accepts "Z" since 3.11;
                # normalize it so "2024-01-15T10:30:00Z" works on 3.10 too.
                value = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
            except ValueError:
                raise InvalidArgumentError(self.get_invalid_datetime_error_message(value))
        if not isinstance(value, datetime):
            raise InvalidArgumentError(self.get_invalid_type_error_message(value))
        if value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        return value

    def get_invalid_datetime_error_message(self, value: str) -> str:
        return f"'{value}' is not a valid ISO datetime"

    def get_invalid_type_error_message(self, value) -> str:
        return f"Value must be a datetime or ISO datetime string, got {type(value).__name__}"
