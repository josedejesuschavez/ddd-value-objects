import pytest
from decimal import Decimal
from src.ddd_value_objects import MoneyValueObject, InvalidArgumentError

def test_money_value_object_valid():
    amount = Decimal("100.50")
    currency = "USD"
    vo1 = MoneyValueObject(amount, currency)
    vo2 = MoneyValueObject(amount, currency)
    
    assert vo1.amount == amount
    assert vo1.currency == currency
    assert vo1.equals(vo2)
    assert repr(vo1) == f"MoneyValueObject(amount=Decimal('{amount}'), currency='{currency}')"
    assert str(vo1) == f"{amount} {currency}"

def test_money_value_object_invalid_amount():
    with pytest.raises(InvalidArgumentError, match="is not a positive decimal"):
        MoneyValueObject(Decimal("-10.0"), "USD")

def test_money_value_object_invalid_currency():
    with pytest.raises(InvalidArgumentError, match="is not a valid ISO 4217 currency code"):
        MoneyValueObject(Decimal("100.0"), "us dollars")

def test_money_value_object_equality():
    from src.ddd_value_objects import StringValueObject
    vo1 = MoneyValueObject(Decimal("100"), "USD")
    vo2 = MoneyValueObject(Decimal("100"), "EUR")
    vo3 = MoneyValueObject(Decimal("50"), "USD")
    
    assert not vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert not vo1.equals(StringValueObject("test"))

def test_money_value_object_add():
    m1 = MoneyValueObject(Decimal("100"), "USD")
    m2 = MoneyValueObject(Decimal("50"), "USD")
    
    result = m1.add(m2)
    
    assert result.amount == Decimal("150")
    assert result.currency == "USD"
    assert isinstance(result, MoneyValueObject)
    assert result is not m1
    assert result is not m2

def test_money_value_object_add_different_currencies():
    m1 = MoneyValueObject(Decimal("100"), "USD")
    m2 = MoneyValueObject(Decimal("50"), "EUR")
    
    with pytest.raises(InvalidArgumentError, match="Cannot add money with different currencies"):
        m1.add(m2)
