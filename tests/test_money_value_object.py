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
    from src.ddd_value_objects import StringValueObject
    vo1 = MoneyValueObject(100, "USD")
    vo2 = MoneyValueObject(100, "EUR")
    vo3 = MoneyValueObject(50, "USD")
    
    assert not vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert not vo1.equals(StringValueObject("test"))

def test_money_value_object_add():
    m1 = MoneyValueObject(100, "USD")
    m2 = MoneyValueObject(50, "USD")
    
    result = m1.add(m2)
    
    assert result.amount == 150
    assert result.currency == "USD"
    assert isinstance(result, MoneyValueObject)
    assert result is not m1
    assert result is not m2

def test_money_value_object_add_different_currencies():
    m1 = MoneyValueObject(100, "USD")
    m2 = MoneyValueObject(50, "EUR")
    
    with pytest.raises(InvalidArgumentError, match="Cannot add money with different currencies"):
        m1.add(m2)
