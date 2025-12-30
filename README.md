# DDD Value Objects for Python

A comprehensive collection of base classes and specialized types for implementing **Domain-Driven Design (DDD)** patterns in Python. This library provides a robust foundation for building maintainable, type-safe, and self-validating domain models using Value Objects and Entities.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Coverage](https://img.shields.io/badge/coverage-93%25-brightgreen.svg)](https://github.com/youruser/ddd-value-objects)

## Key Features

- **Base Classes**: Robust base classes for both Primitive and Composite Value Objects.
- **Immutability**: Designed to be immutable, ensuring domain integrity.
- **Structural Equality**: Value Objects are compared by their attributes, not by identity.
- **Self-Validation**: Built-in validation for common domain types (Emails, UUIDs, URLs, etc.).
- **Strong Typing**: Leverages Python generics for type safety and better IDE support.
- **Entity Support**: Base class for Entities with identity-based equality.

## Installation

Install using `pip`:

```bash
pip install ddd-value-objects
```

Or using `uv`:

```bash
uv add ddd-value-objects
```

## Core Concepts

### Value Objects
In DDD, a **Value Object** is an object that represents a descriptive aspect of the domain with no conceptual identity. They are defined by their attributes and are immutable. Two value objects are considered equal if all their attributes are equal.

### Primitive Value Objects
Wrap single primitive types (`str`, `int`, `float`, `bool`) to give them domain meaning.

### Composite Value Objects
Combine multiple values into a single domain concept (e.g., `Money` which consists of an `amount` and a `currency`).

### Entities
**Entities** have a unique identity that persists over time, regardless of changes to their attributes.

---

## Usage Examples

### 1. Primitive Value Objects

You can extend base classes to create domain-specific types:

```python
from ddd_value_objects import StringValueObject, PositiveIntValueObject, InvalidArgumentError

class UserName(StringValueObject):
    pass

class UserAge(PositiveIntValueObject):
    def __init__(self, value: int):
        super().__init__(value)
        if value > 150:
            raise InvalidArgumentError(f"Age {value} is out of valid range (max 150)")

# Usage
name1 = UserName("Alice")
name2 = UserName("Alice")
age = UserAge(30)

print(name1 == name2)  # True (Structural equality)
print(name1.value)     # "Alice"
```

### 2. Specialized Value Objects

The library includes many pre-built, self-validating types:

```python
from ddd_value_objects import (
    EmailValueObject, 
    UuidValueObject, 
    UrlValueObject, 
    PhoneNumberValueObject,
    CurrencyValueObject
)

email = EmailValueObject("user@example.com")
user_id = UuidValueObject("550e8400-e29b-41d4-a716-446655440000")
website = UrlValueObject("https://github.com")
currency = CurrencyValueObject("USD") # Validates ISO 4217 code
```

### 3. Composite Value Objects (e.g., Money)

Handle complex types that group multiple values:

```python
from ddd_value_objects import MoneyValueObject

price = MoneyValueObject(99.99, "USD")
tax = MoneyValueObject(10.00, "USD")

# Arithmetic operations (if supported by implementation)
total = price.add(tax)

print(total.amount)   # 109.99
print(total.currency) # "USD"
```

### 4. Enum Value Objects

Restrict values to a specific set using an `Enum`:

```python
from enum import Enum
from ddd_value_objects import EnumValueObject, StringValueObject, InvalidArgumentError

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"

class RoleValueObject(EnumValueObject):
    def __init__(self, value: str):
        # Define the valid options
        valid_roles = [StringValueObject(r.value) for r in UserRole]
        
        # Pass the current value as a ValueObject and the list of valid options
        super().__init__(
            StringValueObject(value), 
            valid_roles
        )

# Usage
try:
    role = RoleValueObject("admin")
    print(role.value)  # "admin"
    
    invalid_role = RoleValueObject("guest") # Raises InvalidArgumentError
except InvalidArgumentError as e:
    print(e)
```

### 5. Entities

Use the `Entity` base class for objects with identity:

```python
from ddd_value_objects import Entity, UuidValueObject

class Product(Entity):
    def __init__(self, product_id: str, name: str):
        # Entity expects a string ID which it wraps in a UuidValueObject
        super().__init__(product_id)
        self.name = name

product1 = Product("550e8400-e29b-41d4-a716-446655440000", "Laptop")
product2 = Product("550e8400-e29b-41d4-a716-446655440000", "Updated Laptop Name")

print(product1 == product2) # True (Same identity/ID)
```

---

## Available Value Objects

| Category | Classes |
| :--- | :--- |
| **Primitives** | `StringValueObject`, `IntValueObject`, `FloatValueObject`, `BoolValueObject` |
| **Numeric** | `PositiveIntValueObject`, `PositiveFloatValueObject` |
| **Identity** | `UuidValueObject` |
| **Network** | `EmailValueObject`, `UrlValueObject`, `IpAddressValueObject` |
| **Communication** | `PhoneNumberValueObject`, `CountryCodeValueObject` (ISO 3166-1 alpha-2) |
| **Temporal** | `DateTimeValueObject`, `DateValueObject` (Unix timestamps) |
| **Financial** | `CurrencyValueObject` (ISO 4217), `MoneyValueObject` |
| **Others** | `EnumValueObject`, `CompositeValueObject` |

---

## Development and Testing

We use `uv` for dependency management and `pytest` for testing.

### Setup

```bash
# Clone the repository
git clone https://github.com/youruser/ddd-value-objects.git
cd ddd-value-objects

# Install dependencies
uv sync
```

### Running Tests

```bash
uv run pytest
```

### Coverage Threshold

This project maintains a minimum coverage threshold of **90%**. The CI workflow will automatically fail if coverage falls below this level.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.