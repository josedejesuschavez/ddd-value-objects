from typing import List

from .value_object import ValueObject, Primitives
from .invalid_argument_error import InvalidArgumentError


class EnumValueObject(ValueObject):
    def __init__(self, value: ValueObject, valid_values: List[ValueObject]):
        super().__init__(value.value)
        self._ensure_value_is_valid(value, valid_values)

    def _ensure_value_is_valid(self, value: ValueObject, valid_values: List[ValueObject]) -> None:
        if value not in valid_values:
            raise InvalidArgumentError(
                f"'{value}' is not a valid value. Allowed values are: {valid_values}"
            )

    def equals(self, other: 'ValueObject') -> bool:
        if not isinstance(other, EnumValueObject):
            return False
        return self.value == other.value

    def __repr__(self):
        return f"{self.__class__.__name__}(value={repr(self.value)})"
