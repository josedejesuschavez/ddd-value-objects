from dataclasses import dataclass

from .int_value_object import IntValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class PositiveIntValueObject(IntValueObject):
    def min_value(self) -> int | None:
        return 0

    def get_too_low_error_message(self, value: int, min_value: int) -> str:
        return f"'{value}' is not a positive integer"
