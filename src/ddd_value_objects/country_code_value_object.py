import re

from .invalid_argument_error import InvalidArgumentError
from .string_value_object import StringValueObject


class CountryCodeValueObject(StringValueObject):
    """
    Value Object for ISO 3166-1 alpha-2 country codes.
    """

    def __init__(self, value: str):
        super().__init__(value)
        self._ensure_is_valid_country_code(value)

    def _ensure_is_valid_country_code(self, value: str) -> None:
        if not re.match(r"^[A-Z]{2}$", value):
            raise InvalidArgumentError(
                f"'{value}' is not a valid ISO 3166-1 alpha-2 country code"
            )

    def __repr__(self):
        return f"CountryCodeValueObject(value='{self.value}')"
