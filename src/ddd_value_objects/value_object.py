from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, Any

from .invalid_argument_error import InvalidArgumentError


Primitives = TypeVar('Primitives', int, str, float, bool)


class ValueObject(ABC, Generic[Primitives]):
    def __init__(self, value: Primitives):
        object.__setattr__(self, '_value', value)
        self._ensure_value_is_defined(value)
        object.__setattr__(self, '_initialized', True)

    def __setattr__(self, name: str, value: Any) -> None:
        if getattr(self, '_initialized', False):
            raise TypeError(f"{self.__class__.__name__} is immutable")
        object.__setattr__(self, name, value)

    def __delattr__(self, name: str) -> None:
        if getattr(self, '_initialized', False):
            raise TypeError(f"{self.__class__.__name__} is immutable")
        object.__delattr__(self, name)

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
