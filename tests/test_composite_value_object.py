import pytest
from src.ddd_value_objects.composite_value_object import CompositeValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError

class MockCompositeValueObject(CompositeValueObject[dict]):
    pass

def test_composite_value_object_valid():
    val = {'a': 1, 'b': 2}
    vo = MockCompositeValueObject(val)
    assert vo.value == val
    assert str(vo) == str(val)

def test_composite_value_object_none():
    with pytest.raises(InvalidArgumentError, match="Value must be defined"):
        MockCompositeValueObject(None)

def test_composite_value_object_equality():
    vo1 = MockCompositeValueObject({'a': 1})
    vo2 = MockCompositeValueObject({'a': 1})
    vo3 = MockCompositeValueObject({'a': 2})
    
    assert vo1.equals(vo2)
    assert vo1 == vo2
    assert not vo1.equals(vo3)
    assert vo1 != vo3
    assert vo1 != "not a vo"
    
    class AnotherComposite(CompositeValueObject[dict]):
        pass
    vo4 = AnotherComposite({'a': 1})
    assert not vo1.equals(vo4)
    assert vo1 != vo4

def test_composite_value_object_hash():
    vo1 = MockCompositeValueObject({'a': 1, 'b': 2})
    vo2 = MockCompositeValueObject({'a': 1, 'b': 2})
    vo3 = MockCompositeValueObject({'b': 2, 'a': 1})
    vo4 = MockCompositeValueObject({'a': 1})
    
    assert hash(vo1) == hash(vo2)
    assert hash(vo1) == hash(vo3)
    assert hash(vo1) != hash(vo4)
