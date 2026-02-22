from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal
from typing import TypeVar, Generic, Optional, Any

from .invalid_argument_error import InvalidArgumentError


Primitives = TypeVar('Primitives', int, str, float, bool, Decimal)

@dataclass(frozen=True, slots=True)
class ValueObject(ABC, Generic[Primitives]):
    value: Primitives

    def __post_init__(self):
        self._ensure_value_is_defined(self.value)

    def equals(self, other: Any) -> bool:
        if other is None or other.__class__ != self.__class__:
            return False
        return self == other

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    def _ensure_value_is_defined(value: Optional[Primitives]) -> None:
        if value is None:
            raise InvalidArgumentError("Value must be defined")
