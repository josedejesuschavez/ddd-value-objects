import re
from dataclasses import dataclass

from .string_value_object import StringValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class EmailValueObject(StringValueObject):
    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_valid_email(self.value)

    @staticmethod
    def _ensure_is_valid_email(value: str) -> None:
        if not EmailValueObject.EMAIL_REGEX.match(value):
            raise InvalidArgumentError(f"'{value}' is not a valid email address")
