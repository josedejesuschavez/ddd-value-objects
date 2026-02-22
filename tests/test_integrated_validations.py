from ddd_value_objects import (
    StringValueObject, 
    IntValueObject, 
    FloatValueObject, 
    DecimalValueObject, 
    InvalidArgumentError
)
from decimal import Decimal
import pytest

def test_string_regex_validation():
    class OnlyLetters(StringValueObject):
        def regex_pattern(self):
            return r"^[a-zA-Z]+$"
            
    # Valid
    OnlyLetters("abc")
    
    # Invalid
    with pytest.raises(InvalidArgumentError, match="Value '123' does not match pattern"):
        OnlyLetters("123")

def test_int_range_validation():
    class Score(IntValueObject):
        def min_value(self):
            return 0
        def max_value(self):
            return 100
            
    # Valid
    Score(0)
    Score(50)
    Score(100)
    
    # Invalid too low
    with pytest.raises(InvalidArgumentError, match="Value -1 is less than minimum required 0"):
        Score(-1)
        
    # Invalid too high
    with pytest.raises(InvalidArgumentError, match="Value 101 is greater than maximum allowed 100"):
        Score(101)

def test_float_range_validation():
    class Percentage(FloatValueObject):
        def min_value(self):
            return 0.0
        def max_value(self):
            return 1.0
            
    # Valid
    Percentage(0.5)
    
    # Invalid
    with pytest.raises(InvalidArgumentError, match="Value 1.1 is greater than maximum allowed 1.0"):
        Percentage(1.1)

def test_decimal_range_validation():
    class Price(DecimalValueObject):
        def min_value(self):
            return Decimal("0.00")
            
    # Valid
    Price(Decimal("10.00"))
    
    # Invalid
    with pytest.raises(InvalidArgumentError, match="Value -0.01 is less than minimum required 0.00"):
        Price(Decimal("-0.01"))
