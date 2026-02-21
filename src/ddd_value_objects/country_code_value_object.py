import re
from dataclasses import dataclass

from .invalid_argument_error import InvalidArgumentError
from .string_value_object import StringValueObject


@dataclass(frozen=True, slots=True)
class CountryCodeValueObject(StringValueObject):
    """
    Value Object for ISO 3166-1 alpha-2 country codes.
    """

    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_valid_country_code(self.value)

    @staticmethod
    def _ensure_is_valid_country_code(value: str) -> None:
        if not re.match(r"^[A-Z]{2}$", value):
            raise InvalidArgumentError(
                f"'{value}' is not a valid ISO 3166-1 alpha-2 country code"
            )
