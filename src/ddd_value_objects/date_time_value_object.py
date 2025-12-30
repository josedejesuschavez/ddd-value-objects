from datetime import datetime
from .value_object import ValueObject
from .invalid_argument_error import InvalidArgumentError


class DateTimeValueObject(ValueObject[int]):

    def __init__(self, value: int):
        super().__init__(value)
        self._ensure_is_valid_timestamp(value)

    def _ensure_is_valid_timestamp(self, value: int) -> None:
        try:
            datetime.fromtimestamp(value)
        except (ValueError, OSError, OverflowError):
            raise InvalidArgumentError(f"'{value}' is not a valid Unix timestamp")

    def equals(self, other: 'ValueObject') -> bool:
        if not isinstance(other, DateTimeValueObject):
            return False
        return self.value == other.value

    def __repr__(self):
        return f"DateTimeValueObject(value={self.value})"
