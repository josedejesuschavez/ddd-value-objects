from dataclasses import dataclass
from decimal import Decimal
from .decimal_value_object import DecimalValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class PositiveDecimalValueObject(DecimalValueObject):
    def min_value(self) -> Decimal | None:
        return Decimal("0")

    def get_too_low_error_message(self, value: Decimal, min_value: Decimal) -> str:
        return f"'{value}' is not a positive decimal"
