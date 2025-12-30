from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional

from .invalid_argument_error import InvalidArgumentError

Primitives = TypeVar('Primitives', int, str, float, bool)

class ValueObject(ABC, Generic[Primitives]):
    def __init__(self, value: Primitives):
        self._value = value
        self._ensure_value_is_defined(value)

    @abstractmethod
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

    def _ensure_value_is_defined(self, value: Optional[Primitives]) -> None:
        if value is None:
            raise InvalidArgumentError("Value must be defined")

    @property
    def value(self) -> Primitives:
        return self._value
