from dataclasses import dataclass

from .invalid_argument_error import InvalidArgumentError
from .value_object import ValueObject


@dataclass(frozen=True, slots=True)
class BoolValueObject(ValueObject[bool]):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_value_is_bool(self.value)

    @staticmethod
    def _ensure_value_is_bool(value: bool) -> None:
        if not isinstance(value, bool):
            raise InvalidArgumentError(f"Value must be a boolean, got {type(value)}")
