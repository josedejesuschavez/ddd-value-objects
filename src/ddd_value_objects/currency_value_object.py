import re
from .string_value_object import StringValueObject
from .invalid_argument_error import InvalidArgumentError


class CurrencyValueObject(StringValueObject):
    # Código ISO 4217: 3 letras mayúsculas
    CURRENCY_REGEX = re.compile(r"^[A-Z]{3}$")

    def __init__(self, value: str):
        super().__init__(value)
        self._ensure_is_valid_currency(value)

    def _ensure_is_valid_currency(self, value: str) -> None:
        if not self.CURRENCY_REGEX.match(value):
            raise InvalidArgumentError(f"'{value}' is not a valid ISO 4217 currency code")

    def __repr__(self):
        return f"CurrencyValueObject(value='{self.value}')"
