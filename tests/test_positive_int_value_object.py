import pytest

from src.ddd_value_objects.positive_int_value_object import PositiveIntValueObject
from src.ddd_value_objects.invalid_argument_error import InvalidArgumentError


def test_positive_int_value_object():
    vo1 = PositiveIntValueObject(10)
    vo2 = PositiveIntValueObject(10)
    vo3 = PositiveIntValueObject(20)
    
    assert vo1.value == 10
    assert vo1.equals(vo2)
    assert not vo1.equals(vo3)
    assert repr(vo1) == "PositiveIntValueObject(value=10)"

def test_positive_int_value_object_invalid():
    with pytest.raises(InvalidArgumentError, match="is not a positive integer"):
        PositiveIntValueObject(-1)

def test_positive_int_value_object_zero():
    # En DDD a veces "positivo" incluye el cero dependiendo del negocio,
    # pero aquí hemos definido < 0 como inválido.
    vo = PositiveIntValueObject(0)
    assert vo.value == 0
