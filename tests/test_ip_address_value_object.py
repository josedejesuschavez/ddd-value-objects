import pytest
from src.ddd_value_objects.ip_address_value_object import IpAddressValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError

def test_ip_address_value_object_ipv4():
    ipv4 = "192.168.1.1"
    vo1 = IpAddressValueObject(ipv4)
    vo2 = IpAddressValueObject(ipv4)
    vo3 = IpAddressValueObject("127.0.0.1")
    
    assert vo1.value == ipv4
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert not vo1.equals(ipv4)
    assert repr(vo1) == f"IpAddressValueObject(value='{ipv4}')"

def test_ip_address_value_object_ipv6():
    ipv6 = "2001:db8::1"
    vo1 = IpAddressValueObject(ipv6)
    vo2 = IpAddressValueObject(ipv6)
    
    assert vo1.value == ipv6
    assert vo1.equals(vo2)
    assert repr(vo1) == f"IpAddressValueObject(value='{ipv6}')"

def test_ip_address_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a valid IP address"):
        IpAddressValueObject("not-an-ip")
    
    with pytest.raises(InvalidArgumentError, match="is not a valid IP address"):
        IpAddressValueObject("256.256.256.256")
    
    with pytest.raises(InvalidArgumentError, match="is not a valid IP address"):
        IpAddressValueObject("2001:db8::g1")
