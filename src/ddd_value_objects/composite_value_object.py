from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, Any

from .invalid_argument_error import InvalidArgumentError

T = TypeVar('T', bound=dict)

class CompositeValueObject(ABC, Generic[T]):
    def __init__(self, value: T):
        self._value = value
        self._ensure_value_is_defined(value)

    def equals(self, other: 'CompositeValueObject[T]') -> bool:
        return other.__class__ == self.__class__ and other.value == self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CompositeValueObject):
            return False
        return self.equals(other)

    def __hash__(self) -> int:
        # Los diccionarios no son hasheables, así que convertimos a items ordenados si es posible
        # o usamos una representación inmutable para el hash.
        return hash((self.__class__, tuple(sorted(self._value.items()))))

    def __str__(self) -> str:
        return str(self._value)

    def _ensure_value_is_defined(self, value: Optional[T]) -> None:
        if value is None:
            raise InvalidArgumentError("Value must be defined")

    @property
    def value(self) -> T:
        return self._value
