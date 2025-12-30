import pytest

from src.ddd_value_objects import PhoneNumberValueObject, InvalidArgumentError


def test_phone_number_value_object_valid():
    valid_numbers = [
        "+34600000000",
        "34600000000",
        "+15555555555",
        "15555555555",
        "+441234567890",
    ]
    for number in valid_numbers:
        vo = PhoneNumberValueObject(number)
        assert vo.value == number

def test_phone_number_value_object_normalization():
    vo = PhoneNumberValueObject("+34 600-00-00-00")
    assert vo.value == "+34600000000"
    
    vo2 = PhoneNumberValueObject("(+34) 600 000 000")
    assert vo2.value == "+34600000000"

def test_phone_number_value_object_invalid():
    invalid_numbers = [
        "abc",
        "123",
        "+1234567890123456",
        "00000000",
        "",
    ]
    for number in invalid_numbers:
        with pytest.raises(InvalidArgumentError, match="is not a valid phone number"):
            PhoneNumberValueObject(number)

def test_phone_number_value_object_equality():
    vo1 = PhoneNumberValueObject("+34 600 000 000")
    vo2 = PhoneNumberValueObject("+34600000000")
    assert vo1.equals(vo2)
