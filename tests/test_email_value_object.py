import pytest

from src.ddd_value_objects import EmailValueObject, InvalidArgumentError


def test_email_value_object_valid():
    email_str = "test@example.com"
    vo1 = EmailValueObject(email_str)
    vo2 = EmailValueObject(email_str)
    
    assert vo1.value == email_str
    assert vo1.equals(vo2)
    assert repr(vo1) == f"EmailValueObject(value='{email_str}')"

def test_email_value_object_invalid():
    invalid_emails = [
        "plainaddress",
        "#@%^%#$@#$@#.com",
        "@example.com",
        "Joe Smith <email@example.com>",
        "email.example.com",
        "email@example@example.com",
    ]
    for email in invalid_emails:
        with pytest.raises(InvalidArgumentError, match="is not a valid email address"):
            EmailValueObject(email)

def test_email_value_object_complex_valid():
    valid_emails = [
        "email@example.com",
        "firstname.lastname@example.com",
        "email@subdomain.example.com",
        "firstname+lastname@example.com",
        "1234567890@example.com",
        "email@example-one.com",
        "_______@example.com",
        "email@example.name",
        "email@example.museum",
        "email@example.co.jp",
        "firstname-lastname@example.com",
    ]
    for email in valid_emails:
        vo = EmailValueObject(email)
        assert vo.value == email
