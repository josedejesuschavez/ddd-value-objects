from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Any

from .invalid_argument_error import InvalidArgumentError


Primitives = TypeVar('Primitives', int, str, float, bool)

@dataclass(frozen=True, slots=True)
class ValueObject(ABC, Generic[Primitives]):
    value: Primitives

    def __post_init__(self):
        self._ensure_value_is_defined(self.value)

    def equals(self, other: 'ValueObject[Primitives]') -> bool:
        return other.__class__ == self.__class__ and other.value == self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ValueObject):
            return False
        return self.equals(other)

    def __hash__(self) -> int:
        return hash((self.__class__, self._value))

    def __str__(self) -> str:
        return str(self._value)

    @staticmethod
    def _ensure_value_is_defined(self, value: Optional[Primitives]) -> None:
        if value is None:
            raise InvalidArgumentError("Value must be defined")

    @property
    def value(self) -> Primitives:
        return self._value
