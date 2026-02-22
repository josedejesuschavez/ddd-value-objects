from dataclasses import dataclass

from .int_value_object import IntValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class PositiveIntValueObject(IntValueObject):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_positive(self.value)

    def _ensure_is_positive(self, value: int) -> None:
        if value < 0:
            raise InvalidArgumentError(self.get_not_positive_error_message(value))

    def get_not_positive_error_message(self, value: int) -> str:
        return f"'{value}' is not a positive integer"
