from uuid_value_object import UuidValueObject


class Entity:
    def __init__(self, entity_id: str):
        self.id = UuidValueObject(value=entity_id)

    def equals(self, other: 'Entity') -> bool:
        if not isinstance(other, Entity):
            return False

        return self.id.equals(other.id)
