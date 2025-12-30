# DDD Value Objects

Una colección de clases base para implementar Objetos de Valor (Value Objects) y Entidades siguiendo los principios de Domain-Driven Design (DDD) en Python.

## Características

- Clases base para Objetos de Valor de tipos primitivos (`String`, `Int`, `Float`, `Bool`).
- Soporte para valores numéricos positivos (`PositiveInt`, `PositiveFloat`).
- Soporte para tipos de datos temporales (`DateTime`, `Date`).
- Soporte para `UuidValueObject`, `EmailValueObject`, `PhoneNumberValueObject`, `CountryCodeValueObject` y `UrlValueObject`.
- Objeto compuesto `MoneyValueObject` (cantidad + moneda ISO 4217).
- Clase base para `Entity` con identificación basada en UUID.
- Tipado fuerte y validación de nulidad por defecto.
- Comparación de igualdad estructural para Objetos de Valor e igualdad de identidad para Entidades.

## Instalación

Puedes instalarlo usando `pip`:

```bash
pip install ddd-value-objects
```

O usando `uv`:

```bash
uv add ddd-value-objects
```

## Uso

### Objetos de Valor (Value Objects)

Los Objetos de Valor son inmutables y se definen por sus atributos, no por una identidad única.

```python
from ddd_value_objects.string_value_object import StringValueObject
from ddd_value_objects.int_value_object import IntValueObject

class UserName(StringValueObject):
    pass

class UserAge(IntValueObject):
    def __init__(self, value: int):
        super().__init__(value)
        if value < 0:
            raise ValueError("Age cannot be negative")

name1 = UserName("Alice")
name2 = UserName("Alice")
name3 = UserName("Bob")

print(name1.equals(name2)) # True
print(name1.equals(name3)) # False
```

### UUID Value Object

Especialmente útil para identificadores:

```python
from ddd_value_objects.uuid_value_object import UuidValueObject

user_id = UuidValueObject("550e8400-e29b-41d4-a716-446655440000")
```

### Objetos de Valor Temporales

Para manejar fechas y horas usando tipos primitivos (`int` para timestamps):

```python
from ddd_value_objects import DateTimeValueObject, DateValueObject

# Ambos usan int (Unix Timestamp)
registration = UserRegistrationDate(1698412200) # DateTime
birth = UserBirthDate(631152000)               # Date (1990-01-01)
```

### Entidades (Entities)

Las Entidades tienen una identidad única que las distingue de otras entidades del mismo tipo.

```python
from ddd_value_objects.entity import Entity

class User(Entity):
    def __init__(self, id: str, name: str):
        super().__init__(id)
        self.name = name

user1 = User("550e8400-e29b-41d4-a716-446655440000", "Alice")
user2 = User("550e8400-e29b-41d4-a716-446655440000", "Alice Smith")

print(user1.equals(user2)) # True (misma identidad)
```

## Desarrollo

Si deseas contribuir o ejecutar las pruebas localmente:

1. Instala `uv` si no lo tienes.
2. Sincroniza las dependencias:
   ```bash
   uv sync
   ```
3. Ejecuta los tests:
   ```bash
   uv run pytest
   ```

## Licencia

Este proyecto está bajo la licencia MIT.