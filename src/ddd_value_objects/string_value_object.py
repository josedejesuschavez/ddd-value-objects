from typing import Any
from dataclasses import dataclass

from .invalid_argument_error import InvalidArgumentError
from .value_object import ValueObject, Primitives


@dataclass(frozen=True, slots=True)
class StringValueObject(ValueObject[str]):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_value_is_string(self.value)

    def _ensure_value_is_string(self, value: str) -> None:
        if not isinstance(value, str):
            raise InvalidArgumentError(
                self.get_invalid_type_error_message(value)
            )

    def get_invalid_type_error_message(self, value: Any) -> str:
        return f"Value must be a string, got {type(value)}"
