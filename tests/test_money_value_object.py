import pytest
from src.ddd_value_objects import MoneyValueObject, InvalidArgumentError

def test_money_value_object_valid():
    amount = 100.50
    currency = "USD"
    vo1 = MoneyValueObject(amount, currency)
    vo2 = MoneyValueObject(amount, currency)
    
    assert vo1.amount == amount
    assert vo1.currency == currency
    assert vo1.equals(vo2)
    assert repr(vo1) == f"MoneyValueObject(amount={amount}, currency='{currency}')"
    assert str(vo1) == f"{amount} {currency}"

def test_money_value_object_invalid_amount():
    with pytest.raises(InvalidArgumentError, match="is not a positive float"):
        MoneyValueObject(-10.0, "USD")

def test_money_value_object_invalid_currency():
    with pytest.raises(InvalidArgumentError, match="is not a valid ISO 4217 currency code"):
        MoneyValueObject(100.0, "us dollars")

def test_money_value_object_equality():
    vo1 = MoneyValueObject(100, "USD")
    vo2 = MoneyValueObject(100, "EUR")
    vo3 = MoneyValueObject(50, "USD")
    
    assert not vo1.equals(vo2)
    assert not vo1.equals(vo3)
