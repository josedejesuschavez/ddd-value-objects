import re
from dataclasses import dataclass

from .string_value_object import StringValueObject
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class EmailValueObject(StringValueObject):
    """Email address with canonical storage form.

    The value is normalized (stripped and lowercased) before any
    validation runs, so ``"  User@Example.COM "`` is stored as
    ``user@example.com``. This keeps equality, uniqueness lookups and
    deduplication consistent across the system.
    """

    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    def __post_init__(self):
        self._normalize()
        super().__post_init__()
        self._ensure_is_valid_email(self.value)

    def _normalize(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", self.value.strip().lower())

    def _ensure_is_valid_email(self, value: str) -> None:
        if not EmailValueObject.EMAIL_REGEX.match(value):
            raise InvalidArgumentError(self.get_invalid_email_error_message(value))

    def get_invalid_email_error_message(self, value: str) -> str:
        return f"'{value}' is not a valid email address"
