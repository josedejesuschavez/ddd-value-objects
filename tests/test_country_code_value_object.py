import pytest

from src.ddd_value_objects.country_code_value_object import CountryCodeValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError


def test_country_code_value_object_valid():
    codes = ["US", "ES", "FR", "MX", "AR"]
    for code in codes:
        vo = CountryCodeValueObject(code)
        assert vo.value == code
        assert str(vo) == code

def test_country_code_value_object_equality():
    vo1 = CountryCodeValueObject("ES")
    vo2 = CountryCodeValueObject("ES")
    vo3 = CountryCodeValueObject("US")
    
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)

def test_country_code_value_object_invalid():
    invalid_codes = ["USA", "es", "E1", " ", "E", ""]
    for code in invalid_codes:
        with pytest.raises(InvalidArgumentError, match="is not a valid ISO 3166-1 alpha-2 country code"):
            CountryCodeValueObject(code)

def test_country_code_value_object_repr():
    vo = CountryCodeValueObject("ES")
    assert repr(vo) == "CountryCodeValueObject(value='ES')"
