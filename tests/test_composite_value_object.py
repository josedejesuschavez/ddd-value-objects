from dataclasses import dataclass

import pytest
from src.ddd_value_objects.composite_value_object import CompositeValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError


@dataclass(frozen=True, slots=True)
class MockCompositeValueObject(CompositeValueObject):
    a: int
    b: int

def test_composite_value_object_valid():
    val = {'a': 1, 'b': 2}
    vo = MockCompositeValueObject(a=val['a'], b=val['b'])
    assert vo.a == val['a']
    assert vo.b == val['b']

def test_composite_value_object_equality():
    vo1 = MockCompositeValueObject(a=1, b=0)
    vo2 = MockCompositeValueObject(a=1, b=0)
    vo3 = MockCompositeValueObject(a=2, b=0)
    
    assert vo1.equals(vo2)
    assert vo1 == vo2
    assert not vo1.equals(vo3)
    assert vo1 != vo3
    assert vo1 != "not a vo"

    @dataclass(frozen=True, slots=True)
    class AnotherComposite(CompositeValueObject):
        a: int
    vo4 = AnotherComposite(a=1)
    assert not vo1.equals(vo4)
    assert vo1 != vo4

def test_composite_value_object_hash():
    vo1 = MockCompositeValueObject(a=1, b=2)
    vo2 = MockCompositeValueObject(a=1, b=2)
    vo3 = MockCompositeValueObject(a=1, b=2)
    vo4 = MockCompositeValueObject(a=1, b=0)
    
    assert hash(vo1) == hash(vo2)
    assert hash(vo1) == hash(vo3)
    assert hash(vo1) != hash(vo4)

def test_composite_value_object_field_none():
    with pytest.raises(InvalidArgumentError, match=r"a must be defined"):
        MockCompositeValueObject(a=None, b=2)
    with pytest.raises(InvalidArgumentError, match=r"b must be defined"):
        MockCompositeValueObject(a=1, b=None)
