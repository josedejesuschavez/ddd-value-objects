import re
from typing import Any
from dataclasses import dataclass

from .invalid_argument_error import InvalidArgumentError
from .value_object import ValueObject


@dataclass(frozen=True, slots=True)
class StringValueObject(ValueObject[str]):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_value_is_string(self.value)
        self._ensure_min_length(self.value)
        self._ensure_max_length(self.value)
        self._ensure_matches_regex(self.value)

    def _ensure_value_is_string(self, value: str) -> None:
        if not isinstance(value, str):
            raise InvalidArgumentError(
                self.get_invalid_type_error_message(value)
            )

    def _ensure_min_length(self, value: str) -> None:
        min_length = self.min_length()
        if min_length is not None and len(value) < min_length:
            raise InvalidArgumentError(
                self.get_too_short_error_message(value, min_length)
            )

    def _ensure_max_length(self, value: str) -> None:
        max_length = self.max_length()
        if max_length is not None and len(value) > max_length:
            raise InvalidArgumentError(
                self.get_too_long_error_message(value, max_length)
            )

    def _ensure_matches_regex(self, value: str) -> None:
        pattern = self.regex_pattern()
        if pattern is not None:
            if not re.match(pattern, value):
                raise InvalidArgumentError(
                    self.get_invalid_regex_error_message(value, pattern)
                )

    def min_length(self) -> int | None:
        return None

    def max_length(self) -> int | None:
        return None

    def regex_pattern(self) -> str | None:
        return None

    def get_invalid_type_error_message(self, value: Any) -> str:
        return f"Value must be a string, got {type(value)}"

    def get_too_short_error_message(self, value: str, min_length: int) -> str:
        return f"Value is too short. Minimum length is {min_length}, but got {len(value)}"

    def get_too_long_error_message(self, value: str, max_length: int) -> str:
        return f"Value is too long. Maximum length is {max_length}, but got {len(value)}"

    def get_invalid_regex_error_message(self, value: str, pattern: str) -> str:
        return f"Value '{value}' does not match pattern '{pattern}'"

    def get_too_short_error_message_template(self):
        return "Value is too short. Minimum length is {min_length}"

    def get_too_long_error_message_template(self):
        return "Value is too long. Maximum length is {max_length}"