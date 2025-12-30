from .composite_value_object import CompositeValueObject
from .positive_float_value_object import PositiveFloatValueObject
from .currency_value_object import CurrencyValueObject
from .invalid_argument_error import InvalidArgumentError


class MoneyValueObject(CompositeValueObject[dict]):

    def __init__(self, amount: float, currency: str):
        self._amount_vo = PositiveFloatValueObject(amount)
        self._currency_vo = CurrencyValueObject(currency)
        super().__init__({
            'amount': self._amount_vo.value,
            'currency': self._currency_vo.value
        })

    @property
    def amount(self) -> float:
        return self._amount_vo.value

    @property
    def currency(self) -> str:
        return self._currency_vo.value

    def add(self, other: 'MoneyValueObject') -> 'MoneyValueObject':
        if self.currency != other.currency:
            raise InvalidArgumentError("Cannot add money with different currencies")
        return MoneyValueObject(self.amount + other.amount, self.currency)

    def equals(self, other: 'CompositeValueObject') -> bool:
        if not isinstance(other, MoneyValueObject):
            return False
        return (self.amount == other.amount and 
                self.currency == other.currency)

    def __repr__(self):
        return f"MoneyValueObject(amount={self.amount}, currency='{self.currency}')"

    def __str__(self):
        return f"{self.amount} {self.currency}"
