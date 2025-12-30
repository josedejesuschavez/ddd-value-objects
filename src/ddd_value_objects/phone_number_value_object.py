import re

from .string_value_object import StringValueObject
from .invalid_argument_error import InvalidArgumentError


class PhoneNumberValueObject(StringValueObject):
    PHONE_REGEX = re.compile(r"^\+?[1-9]\d{6,14}$")

    def __init__(self, value: str):
        clean_value = self._clean_number(value)
        super().__init__(clean_value)
        self._ensure_is_valid_phone(clean_value)

    def _clean_number(self, value: str) -> str:
        if not isinstance(value, str):
            return value
        return re.sub(r"[\s\-\(\)]", "", value)

    def _ensure_is_valid_phone(self, value: str) -> None:
        if not self.PHONE_REGEX.match(value):
            raise InvalidArgumentError(f"'{value}' is not a valid phone number")

    def __repr__(self):
        return f"PhoneNumberValueObject(value='{self.value}')"
