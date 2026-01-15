from decimal import Decimal
from .value_object import ValueObject


class DecimalValueObject(ValueObject[Decimal]):

    def __init__(self, value: Decimal):
        super().__init__(value)

    def equals(self, other: 'ValueObject') -> bool:
        if not isinstance(other, DecimalValueObject):
            return False
        return self.value == other.value

    def __repr__(self):
        return f"DecimalValueObject(value={self.value})"
