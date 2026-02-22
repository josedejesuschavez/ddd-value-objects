from dataclasses import dataclass
from typing import List

from .value_object import ValueObject, Primitives
from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class EnumValueObject(ValueObject):
    def __init__(self, value: Primitives, valid_values: List[Primitives]):
        self._ensure_value_is_valid(value, valid_values)
        super().__init__(value)

    def __post_init__(self):
        super().__post_init__()

    @staticmethod
    def _ensure_value_is_valid(value: ValueObject, valid_values: List[ValueObject]) -> None:
        if value not in valid_values:
            raise InvalidArgumentError(
                f"'{value}' is not a valid value. Allowed values are: {valid_values}"
            )
