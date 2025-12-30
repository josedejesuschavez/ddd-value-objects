import re

from .string_value_object import StringValueObject
from .invalid_argument_error import InvalidArgumentError


class EmailValueObject(StringValueObject):
    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    def __init__(self, value: str):
        super().__init__(value)
        self._ensure_is_valid_email(value)

    def _ensure_is_valid_email(self, value: str) -> None:
        if not self.EMAIL_REGEX.match(value):
            raise InvalidArgumentError(f"'{value}' is not a valid email address")

    def __repr__(self):
        return f"EmailValueObject(value='{self.value}')"
