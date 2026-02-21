from dataclasses import dataclass

from .value_object import ValueObject


@dataclass(frozen=True, slots=True)
class BoolValueObject(ValueObject[bool]):
    def __post_init__(self):
        super().__post_init__()

        if not isinstance(self.value, bool):
            raise TypeError(f"Value must be a boolean, got {type(self.value)}")
