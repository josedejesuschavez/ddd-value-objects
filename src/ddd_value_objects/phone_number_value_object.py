import re
from dataclasses import dataclass

from .string_value_object import StringValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class PhoneNumberValueObject(StringValueObject):
    PHONE_REGEX = re.compile(r"^\+?[1-9]\d{6,14}$")

    def __init__(self, value: str):
        clean_value = self._clean_number(value)
        super().__init__(clean_value)

    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_valid_phone(self.value)

    @staticmethod
    def _clean_number(value: str) -> str:
        if not isinstance(value, str):
            return value
        return re.sub(r"[\s\-\(\)]", "", value)

    @staticmethod
    def _ensure_is_valid_phone(value: str) -> None:
        if not PhoneNumberValueObject.PHONE_REGEX.match(value):
            raise InvalidArgumentError(f"'{value}' is not a valid phone number")
