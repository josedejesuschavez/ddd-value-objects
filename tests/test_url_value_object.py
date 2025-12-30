import pytest

from src.ddd_value_objects.url_value_object import UrlValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError


def test_url_value_object_valid():
    valid_urls = [
        "http://google.com",
        "https://google.com",
        "https://www.google.com",
        "https://google.com/search?q=test",
        "https://google.com:8080",
        "http://localhost",
        "http://127.0.0.1",
        "ftp://files.example.com"
    ]
    for url in valid_urls:
        vo = UrlValueObject(url)
        assert vo.value == url

def test_url_value_object_equality():
    url = "https://google.com"
    vo1 = UrlValueObject(url)
    vo2 = UrlValueObject(url)
    vo3 = UrlValueObject("https://other.com")
    
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)

def test_url_value_object_invalid():
    invalid_urls = [
        "google.com",
        "htt://google.com",
        "https://",
        "https:// google.com",
        "just-a-string"
    ]
    for url in invalid_urls:
        with pytest.raises(InvalidArgumentError, match="is not a valid URL"):
            UrlValueObject(url)

def test_url_value_object_repr():
    url = "https://google.com"
    vo = UrlValueObject(url)
    assert repr(vo) == f"UrlValueObject(value='{url}')"
