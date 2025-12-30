import pytest

from enum import Enum

from src.ddd_value_objects import ValueObject, StringValueObject, IntValueObject, FloatValueObject
from src.ddd_value_objects.enum_value_object import EnumValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError
from src.ddd_value_objects.value_object import Primitives


class Colors(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"

class ColorValueObject(EnumValueObject):
    def __init__(self, value: Primitives):
        super().__init__(value, [color.value for color in Colors])

def test_enum_value_object_valid():
    vo = ColorValueObject("red")
    assert vo.value == "red"
    assert str(vo) == "red"

def test_enum_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a valid value"):
        ColorValueObject("yellow")

def test_enum_value_object_equality():
    vo1 = ColorValueObject("blue")
    vo2 = ColorValueObject("blue")
    vo3 = ColorValueObject("green")
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert not vo1.equals(StringValueObject("blue"))

def test_enum_value_object_repr():
    vo = ColorValueObject("red")
    assert repr(vo) == "ColorValueObject(value='red')"

def test_enum_value_object_with_other_value_objects():
    from src.ddd_value_objects.string_value_object import StringValueObject
    
    class Tag(StringValueObject):
        pass
    
    tag1 = Tag("urgent")
    tag2 = Tag("normal")
    tag3 = Tag("low")
    
    class PriorityVO(EnumValueObject):
        def __init__(self, value: Tag):
            super().__init__(value, [tag1, tag2, tag3])

    vo = PriorityVO(Tag("urgent"))
    assert vo.value == tag1
    
    with pytest.raises(InvalidArgumentError):
        PriorityVO(Tag("info"))

def test_enum_value_object_with_int():
    class RatingVO(EnumValueObject):
        def __init__(self, value: IntValueObject):
            super().__init__(value, [IntValueObject(1), IntValueObject(2), IntValueObject(3), IntValueObject(4), IntValueObject(5)])
    
    vo = RatingVO(IntValueObject(3))
    assert vo.value == IntValueObject(3)
    
    with pytest.raises(InvalidArgumentError):
        RatingVO(IntValueObject(6))

def test_enum_value_object_with_float():
    class TaxVO(EnumValueObject):
        def __init__(self, value: FloatValueObject):
            super().__init__(value, [FloatValueObject(0.0), FloatValueObject(0.1), FloatValueObject(0.21)])
    
    vo = TaxVO(FloatValueObject(0.21))
    assert vo.value == FloatValueObject(0.21)
    
    with pytest.raises(InvalidArgumentError):
        TaxVO(FloatValueObject(0.15))
