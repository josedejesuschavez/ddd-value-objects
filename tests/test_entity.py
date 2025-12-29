from src.ddd_value_objects.entity import Entity


def test_entity_creation_and_id():
    entity_id = "550e8400-e29b-41d4-a716-446655440000"
    entity = Entity(entity_id)
    assert entity.id.value == entity_id

def test_entity_equality():
    id1 = "550e8400-e29b-41d4-a716-446655440000"
    id2 = "550e8400-e29b-41d4-a716-446655440001"
    
    entity1 = Entity(id1)
    entity2 = Entity(id1)
    entity3 = Entity(id2)
    
    assert entity1.equals(entity2)
    assert not entity1.equals(entity3)
    assert not entity1.equals("not an entity")
