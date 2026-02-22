from dataclasses import dataclass
from decimal import Decimal
from .composite_value_object import CompositeValueObject
from .positive_decimal_value_object import PositiveDecimalValueObject
from .currency_value_object import CurrencyValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class MoneyValueObject(CompositeValueObject):
    amount: Decimal
    currency: str

    def __post_init__(self):
        super().__post_init__()
        PositiveDecimalValueObject(self.amount)
        CurrencyValueObject(self.currency)

    def add(self, other: 'MoneyValueObject') -> 'MoneyValueObject':
        if self.currency != other.currency:
            raise InvalidArgumentError("Cannot add money with different currencies")
        return MoneyValueObject(self.amount + other.amount, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"
