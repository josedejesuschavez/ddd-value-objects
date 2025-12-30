from .positive_float_value_object import PositiveFloatValueObject
from .currency_value_object import CurrencyValueObject


class MoneyValueObject:

    def __init__(self, amount: float, currency: str):
        self._amount = PositiveFloatValueObject(amount)
        self._currency = CurrencyValueObject(currency)

    @property
    def amount(self) -> float:
        return self._amount.value

    @property
    def currency(self) -> str:
        return self._currency.value

    def equals(self, other: 'MoneyValueObject') -> bool:
        if not isinstance(other, MoneyValueObject):
            return False
        return (self.amount == other.amount and 
                self.currency == other.currency)

    def __repr__(self):
        return f"MoneyValueObject(amount={self.amount}, currency='{self.currency}')"

    def __str__(self):
        return f"{self.amount} {self.currency}"
