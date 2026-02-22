from dataclasses import dataclass

from .invalid_argument_error import InvalidArgumentError
from .value_object import ValueObject


@dataclass(frozen=True, slots=True)
class FloatValueObject(ValueObject[float]):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_value_is_float(self.value)

    @staticmethod
    def _ensure_value_is_float(value) -> None:
        if not isinstance(value, float):
            raise InvalidArgumentError(f"Value must be a float, got {type(value)}")
