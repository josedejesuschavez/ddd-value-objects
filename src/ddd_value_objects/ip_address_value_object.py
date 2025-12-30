import ipaddress

from .invalid_argument_error import InvalidArgumentError
from .string_value_object import StringValueObject


class IpAddressValueObject(StringValueObject):

    def __init__(self, value: str):
        super().__init__(value)
        self._ensure_is_valid_ip(value)

    def _ensure_is_valid_ip(self, value: str) -> None:
        try:
            ipaddress.ip_address(value)
        except ValueError:
            raise InvalidArgumentError(f"'{value}' is not a valid IP address")

    def equals(self, other: 'ValueObject') -> bool:
        if not isinstance(other, IpAddressValueObject):
            return False
        return self.value == other.value

    def __repr__(self):
        return f"IpAddressValueObject(value='{self.value}')"
