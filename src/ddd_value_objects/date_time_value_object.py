from dataclasses import dataclass
from datetime import datetime
from .value_object import ValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class DateTimeValueObject(ValueObject[int]):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_valid_timestamp(self.value)

    def _ensure_is_valid_timestamp(self, value: int) -> None:
        try:
            datetime.fromtimestamp(value)
        except (ValueError, OSError, OverflowError):
            raise InvalidArgumentError(self.get_invalid_timestamp_error_message(value))

    def get_invalid_timestamp_error_message(self, value: int) -> str:
        return f"'{value}' is not a valid Unix timestamp"
