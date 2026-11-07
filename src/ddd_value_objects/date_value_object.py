from dataclasses import dataclass
from datetime import date, datetime

from .value_object import ValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class DateValueObject(ValueObject[date]):
    """Wraps a ``date``, accepting ISO strings ("2024-01-15") and
    coercing them transparently.

    ``datetime`` is rejected explicitly even though it subclasses
    ``date``: silently dropping its time component would hide
    information. Use ``DateTimeValueObject`` for datetimes.
    """

    def __init__(self, value: date | str):
        super().__init__(self._parse(value))

    def _parse(self, value: date | str) -> date:
        if isinstance(value, datetime):
            raise InvalidArgumentError(self.get_invalid_type_error_message(value))
        if isinstance(value, date):
            return value
        if isinstance(value, str):
            try:
                return date.fromisoformat(value.strip())
            except ValueError:
                raise InvalidArgumentError(self.get_invalid_date_error_message(value))
        raise InvalidArgumentError(self.get_invalid_type_error_message(value))

    def get_invalid_date_error_message(self, value: str) -> str:
        return f"'{value}' is not a valid ISO date (YYYY-MM-DD)"

    def get_invalid_type_error_message(self, value) -> str:
        return f"Value must be a date or ISO date string, got {type(value).__name__}"
