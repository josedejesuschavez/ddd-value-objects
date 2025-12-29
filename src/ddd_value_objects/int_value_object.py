from .value_object import ValueObject


class IntValueObject(ValueObject[int]):

    def __init__(self, value: int):
        super().__init__(value)

    def equals(self, other: 'ValueObject') -> bool:
        if not isinstance(other, IntValueObject):
            return False
        return self.value == other.value

    def __repr__(self):
        return f"IntValueObject(value={self.value})"
