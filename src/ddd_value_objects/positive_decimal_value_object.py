from dataclasses import dataclass
from decimal import Decimal
from .decimal_value_object import DecimalValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class PositiveDecimalValueObject(DecimalValueObject):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_positive(self.value)

    @staticmethod
    def _ensure_is_positive(value: Decimal) -> None:
        if value < 0:
            raise InvalidArgumentError(f"'{value}' is not a positive decimal")
