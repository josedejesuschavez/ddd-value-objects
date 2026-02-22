import ipaddress
from dataclasses import dataclass

from .invalid_argument_error import InvalidArgumentError
from .string_value_object import StringValueObject


@dataclass(frozen=True, slots=True)
class IpAddressValueObject(StringValueObject):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_valid_ip(self.value)

    def _ensure_is_valid_ip(self, value: str) -> None:
        try:
            ipaddress.ip_address(value)
        except ValueError:
            raise InvalidArgumentError(self.get_invalid_ip_error_message(value))

    def get_invalid_ip_error_message(self, value: str) -> str:
        return f"'{value}' is not a valid IP address"
