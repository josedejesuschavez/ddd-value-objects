import uuid
from dataclasses import dataclass

from .invalid_argument_error import InvalidArgumentError
from .value_object import ValueObject, Primitives


@dataclass(frozen=True, slots=True)
class UuidValueObject(ValueObject[str]):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_validate_is_uuid(self.value)

    @staticmethod
    def _ensure_validate_is_uuid(value: str):
        try:
            uuid.UUID(value)
        except ValueError:
            raise InvalidArgumentError(message=f"'{value}' is not a valid UUID.")
