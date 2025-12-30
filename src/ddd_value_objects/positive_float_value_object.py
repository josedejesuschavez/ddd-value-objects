from .float_value_object import FloatValueObject
from .invalid_argument_error import InvalidArgumentError


class PositiveFloatValueObject(FloatValueObject):

    def __init__(self, value: float):
        super().__init__(value)
        self._ensure_is_positive(value)

    def _ensure_is_positive(self, value: float) -> None:
        if value < 0:
            raise InvalidArgumentError(f"'{value}' is not a positive float")

    def __repr__(self):
        return f"PositiveFloatValueObject(value={self.value})"
