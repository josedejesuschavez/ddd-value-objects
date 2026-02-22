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
        self._ensure_is_within_range(self.value)

    def _ensure_value_is_decimal(self, value: Decimal) -> None:
        if not isinstance(value, Decimal):
            raise InvalidArgumentError(
                self.get_invalid_type_error_message(value)
            )

    def _ensure_is_within_range(self, value: Decimal) -> None:
        min_value = self.min_value()
        max_value = self.max_value()

        if min_value is not None and value < min_value:
            raise InvalidArgumentError(self.get_too_low_error_message(value, min_value))

        if max_value is not None and value > max_value:
            raise InvalidArgumentError(self.get_too_high_error_message(value, max_value))

    def min_value(self) -> Decimal | None:
        return None

    def max_value(self) -> Decimal | None:
        return None

    def get_invalid_type_error_message(self, value: Any) -> str:
        return f"Value must be a decimal, got {type(value)}"

    def get_too_low_error_message(self, value: Decimal, min_value: Decimal) -> str:
        return f"Value {value} is less than minimum required {min_value}"

    def get_too_high_error_message(self, value: Decimal, max_value: Decimal) -> str:
        return f"Value {value} is greater than maximum allowed {max_value}"

    def get_too_low_error_message_template(self):
        return "Value is less than minimum required {min_value}"

    def get_too_high_error_message_template(self):
        return "Value is greater than maximum allowed {max_value}"
