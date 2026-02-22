from ddd_value_objects import StringValueObject, InvalidArgumentError
import pytest

def test_string_value_object_min_length():
    class ShortString(StringValueObject):
        def min_length(self):
            return 5
            
    # Valid
    ShortString("12345")
    ShortString("123456")
    
    # Invalid
    with pytest.raises(InvalidArgumentError, match="Value is too short. Minimum length is 5, but got 4"):
        ShortString("1234")

def test_string_value_object_max_length():
    class LongString(StringValueObject):
        def max_length(self):
            return 10
            
    # Valid
    LongString("1234567890")
    LongString("123")
    
    # Invalid
    with pytest.raises(InvalidArgumentError, match="Value is too long. Maximum length is 10, but got 11"):
        LongString("12345678901")

def test_string_value_object_both_lengths():
    class RangeString(StringValueObject):
        def min_length(self):
            return 3
        def max_length(self):
            return 5
            
    # Valid
    RangeString("123")
    RangeString("1234")
    RangeString("12345")
    
    # Invalid too short
    with pytest.raises(InvalidArgumentError, match="Value is too short"):
        RangeString("12")
        
    # Invalid too long
    with pytest.raises(InvalidArgumentError, match="Value is too long"):
        RangeString("123456")

def test_custom_length_error_messages():
    class CustomMessageString(StringValueObject):
        def min_length(self):
            return 5
        def get_too_short_error_message(self, value, min_length):
            return f"Demasiado corto: {len(value)} < {min_length}"
            
    with pytest.raises(InvalidArgumentError, match="Demasiado corto: 4 < 5"):
        CustomMessageString("1234")
