from dataclasses import dataclass

from .value_object import ValueObject, Primitives


@dataclass(frozen=True, slots=True)
class StringValueObject(ValueObject[str]):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_value_is_string(self.value)

    @staticmethod
    def _ensure_value_is_string(value) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Value must be a string, got {type(value)}")
