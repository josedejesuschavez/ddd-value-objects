from value_object import ValueObject


class FloatValueObject(ValueObject[float]):

    def __init__(self, value: float):
        super().__init__(value)

    def equals(self, other: 'ValueObject') -> bool:
        if not isinstance(other, FloatValueObject):
            return False
        return self.value == other.value

    def __repr__(self):
        return f"FloatValueObject(value={self.value})"
