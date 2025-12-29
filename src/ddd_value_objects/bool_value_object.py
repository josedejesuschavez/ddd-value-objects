from value_object import ValueObject


class BoolValueObject(ValueObject[bool]):

    def __init__(self, value: bool):
        super().__init__(value)

    def equals(self, other: 'ValueObject') -> bool:
        if not isinstance(other, BoolValueObject):
            return False
        return self.value == other.value

    def __repr__(self):
        return f"BoolValueObject(value={self.value})"
