import re
from dataclasses import dataclass

from .string_value_object import StringValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class CurrencyValueObject(StringValueObject):
    CURRENCY_REGEX = re.compile(r"^[A-Z]{3}$")

    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_valid_currency(self.value)

    @staticmethod
    def _ensure_is_valid_currency(value: str) -> None:
        if not CurrencyValueObject.CURRENCY_REGEX.match(value):
            raise InvalidArgumentError(f"'{value}' is not a valid ISO 4217 currency code")
