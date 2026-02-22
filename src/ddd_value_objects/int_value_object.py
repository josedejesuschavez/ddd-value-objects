from typing import Any
from dataclasses import dataclass

from .invalid_argument_error import InvalidArgumentError
from .value_object import ValueObject


@dataclass(frozen=True, slots=True)
class IntValueObject(ValueObject[int]):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_value_is_integer(self.value)

    def _ensure_value_is_integer(self, value: int) -> None:
        if not isinstance(value, int):
            raise InvalidArgumentError(
                self.get_invalid_type_error_message(value)
            )

    def get_invalid_type_error_message(self, value: Any) -> str:
        return f"Value must be a integer, got {type(value)}"
