from dataclasses import dataclass
from decimal import Decimal

from .invalid_argument_error import InvalidArgumentError
from .value_object import ValueObject


@dataclass(frozen=True, slots=True)
class DecimalValueObject(ValueObject[Decimal]):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_value_is_decimal(self.value)

    @staticmethod
    def _ensure_value_is_decimal(value) -> None:
        if not isinstance(value, Decimal):
            raise InvalidArgumentError(f"Value must be a decimal, got {type(value)}")
