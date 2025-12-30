import pytest

from src.ddd_value_objects.uuid_value_object import UuidValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError

def test_uuid_value_object():
    valid_uuid = "550e8400-e29b-41d4-a716-446655440000"
    vo1 = UuidValueObject(valid_uuid)
    vo2 = UuidValueObject(valid_uuid)
    
    assert vo1.value == valid_uuid
    assert vo1.equals(vo2)
    assert repr(vo1) == f"UuidValueObject(value='{valid_uuid}')"

def test_uuid_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a valid UUID"):
        UuidValueObject("invalid-uuid")
