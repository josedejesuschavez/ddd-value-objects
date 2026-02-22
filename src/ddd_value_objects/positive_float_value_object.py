from dataclasses import dataclass

from .float_value_object import FloatValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class PositiveFloatValueObject(FloatValueObject):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_positive(self.value)

    @staticmethod
    def _ensure_is_positive(value: float) -> None:
        if value < 0:
            raise InvalidArgumentError(f"'{value}' is not a positive float")
