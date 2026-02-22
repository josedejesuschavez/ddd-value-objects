from typing import Any
from dataclasses import dataclass
from decimal import Decimal

from .invalid_argument_error import InvalidArgumentError
from .value_object import ValueObject


@dataclass(frozen=True, slots=True)
class DecimalValueObject(ValueObject[Decimal]):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_value_is_decimal(self.value)

    def _ensure_value_is_decimal(self, value: Decimal) -> None:
        if not isinstance(value, Decimal):
            raise InvalidArgumentError(
                self.get_invalid_type_error_message(value)
            )

    def get_invalid_type_error_message(self, value: Any) -> str:
        return f"Value must be a decimal, got {type(value)}"
