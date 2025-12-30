import re

from .string_value_object import StringValueObject
from .invalid_argument_error import InvalidArgumentError


class UrlValueObject(StringValueObject):
    URL_REGEX = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def __init__(self, value: str):
        super().__init__(value)
        self._ensure_is_valid_url(value)

    def _ensure_is_valid_url(self, value: str) -> None:
        if not self.URL_REGEX.match(value):
            raise InvalidArgumentError(f"'{value}' is not a valid URL")

    def __repr__(self):
        return f"UrlValueObject(value='{self.value}')"
