from value_object import ValueObject


class StringValueObject(ValueObject[str]):

    def __init__(self, value: str):
        super().__init__(value)

    def equals(self, other: 'ValueObject[Primitives]') -> bool:
        if not isinstance(other, StringValueObject):
            return False
        return self.value == other.value

    def __repr__(self):
        return f"StringValueObject(value='{self.value}')"
