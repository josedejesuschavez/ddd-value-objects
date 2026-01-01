from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, Any

from .invalid_argument_error import InvalidArgumentError

T = TypeVar('T', bound=dict)

class CompositeValueObject(ABC, Generic[T]):
    def __init__(self, value: T):
        # Convert dictionary to a more immutable form if possible, 
        # but at least prevent reassignment of _value
        self._ensure_value_is_defined(value)
        object.__setattr__(self, '_value', dict(value))
        object.__setattr__(self, '_initialized', True)

    def __setattr__(self, name: str, value: Any) -> None:
        if getattr(self, '_initialized', False):
            raise TypeError(f"{self.__class__.__name__} is immutable")
        object.__setattr__(self, name, value)

    def __delattr__(self, name: str) -> None:
        if getattr(self, '_initialized', False):
            raise TypeError(f"{self.__class__.__name__} is immutable")
        object.__delattr__(self, name)

    @property
    def value(self) -> T:
        # Return a copy to prevent mutation of the internal dictionary
        return dict(self._value)

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

