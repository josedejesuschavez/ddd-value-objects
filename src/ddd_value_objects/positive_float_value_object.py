from dataclasses import dataclass

from .float_value_object import FloatValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class PositiveFloatValueObject(FloatValueObject):
    def min_value(self) -> float | None:
        return 0.0

    def get_too_low_error_message(self, value: float, min_value: float) -> str:
        return f"'{value}' is not a positive float"
