from abc import ABC
from dataclasses import dataclass, fields
from typing import Any

from .invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class CompositeValueObject(ABC):
    def __post_init__(self):
        for field in fields(self):
            field_name = field.name
            value = getattr(self, field_name)
            self._ensure_value_is_defined(value, field_name)

    def equals(self, other: Any) -> bool:
        if other is None or other.__class__ != self.__class__:
            return False
        return self == other

    @staticmethod
    def _ensure_value_is_defined(value: Any, field_name: str = "Value") -> None:
        if value is None:
            raise InvalidArgumentError(f"{field_name} must be defined")

