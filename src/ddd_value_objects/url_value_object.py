import re
from dataclasses import dataclass

from .string_value_object import StringValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class UrlValueObject(StringValueObject):
    URL_REGEX = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_valid_url(self.value)

    @staticmethod
    def _ensure_is_valid_url(value: str) -> None:
        if not UrlValueObject.URL_REGEX.match(value):
            raise InvalidArgumentError(f"'{value}' is not a valid URL")
