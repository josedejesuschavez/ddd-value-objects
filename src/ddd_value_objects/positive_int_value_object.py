from .int_value_object import IntValueObject
from .invalid_argument_error import InvalidArgumentError


class PositiveIntValueObject(IntValueObject):

    def __init__(self, value: int):
        super().__init__(value)
        self._ensure_is_positive(value)

    def _ensure_is_positive(self, value: int) -> None:
        if value < 0:
            raise InvalidArgumentError(f"'{value}' is not a positive integer")

    def __repr__(self):
        return f"PositiveIntValueObject(value={self.value})"
