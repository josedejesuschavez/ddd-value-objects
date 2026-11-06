from dataclasses import dataclass

from .float_value_object import FloatValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class PositiveFloatValueObject(FloatValueObject):
    def min_value(self) -> float | None:
        return 0.0

    def get_too_low_error_message(self, value: float, min_value: float) -> str:
        return f"'{value}' is not a positive float"

    def _ensure_is_within_range(self, value: float) -> None:
        min_value = self.min_value()
        if min_value is not None and value <= min_value:
            raise InvalidArgumentError(self.get_too_low_error_message(value, min_value))
        super()._ensure_is_within_range(value)
