from decimal import Decimal
from .decimal_value_object import DecimalValueObject
from .invalid_argument_error import InvalidArgumentError


class PositiveDecimalValueObject(DecimalValueObject):

    def __init__(self, value: Decimal):
        super().__init__(value)
        self._ensure_is_positive(value)

    def _ensure_is_positive(self, value: Decimal) -> None:
        if value < 0:
            raise InvalidArgumentError(f"'{value}' is not a positive decimal")

    def __repr__(self):
        return f"PositiveDecimalValueObject(value={self.value})"
