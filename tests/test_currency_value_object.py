import pytest
from src.ddd_value_objects import CurrencyValueObject, InvalidArgumentError

def test_currency_value_object_valid():
    vo = CurrencyValueObject("USD")
    assert vo.value == "USD"
    assert repr(vo) == "CurrencyValueObject(value='USD')"

def test_currency_value_object_invalid():
    with pytest.raises(InvalidArgumentError):
        CurrencyValueObject("US dollars")
    
    with pytest.raises(InvalidArgumentError):
        CurrencyValueObject("US")
    
    with pytest.raises(InvalidArgumentError):
        CurrencyValueObject("USDE")

def test_currency_value_object_equality():
    vo1 = CurrencyValueObject("USD")
    vo2 = CurrencyValueObject("USD")
    vo3 = CurrencyValueObject("EUR")
    
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert not vo1.equals("USD")
