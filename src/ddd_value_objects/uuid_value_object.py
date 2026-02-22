import uuid
from dataclasses import dataclass

from .invalid_argument_error import InvalidArgumentError
from .value_object import ValueObject, Primitives


@dataclass(frozen=True, slots=True)
class UuidValueObject(ValueObject[str]):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_validate_is_uuid(self.value)

    def _ensure_validate_is_uuid(self, value: str):
        try:
            uuid.UUID(value)
        except ValueError:
            raise InvalidArgumentError(message=self.get_invalid_uuid_error_message(value))

    def get_invalid_uuid_error_message(self, value: str) -> str:
        return f"'{value}' is not a valid UUID."
