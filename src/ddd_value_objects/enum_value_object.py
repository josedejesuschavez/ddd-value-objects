from dataclasses import dataclass
from typing import List, Any

from .value_object import ValueObject, Primitives
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class EnumValueObject(ValueObject):
    def __init__(self, value: Primitives, valid_values: List[Primitives]):
        self._ensure_value_is_valid(value, valid_values)
        super().__init__(value)

    def _ensure_value_is_valid(self, value: Any, valid_values: List[Any]) -> None:
        if value not in valid_values:
            raise InvalidArgumentError(
                self.get_invalid_enum_error_message(value, valid_values)
            )

    def get_invalid_enum_error_message(self, value: Any, valid_values: List[Any]) -> str:
        return f"'{value}' is not a valid value. Allowed values are: {valid_values}"
