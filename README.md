# __hash__-__eq__-magical-methods
Examples of Python classes implementing comparison, hashing, and validation for unique objects, with various use cases such as books, shapes, points, and transactions.
# ClassObjects-Python-Examples

## Overview
This repository contains examples of Python classes that demonstrate the principles of object comparison, hashing, and attribute validation. Each example is implemented in a separate file and covers different use cases. The code is designed to help understand object equality and uniqueness in Python, useful for creating dictionary keys, set elements, and more.

## Classes Included

### 1. `Point` Class (`ex33.py`)
A class that represents a point in a 2D space, defined by its x and y coordinates. Points with the same coordinates are considered equal and have the same hash value. This enables their use as dictionary keys.

**Key Features:**
- `__eq__` and `__hash__` methods for equality and hashing based on coordinates.
- Example usage for dictionary keys with unique points.

### 2. `Book` Class (`tx1.py`)
A class to represent a book, uniquely identified by its title and author. Validations ensure the title and author are within acceptable lengths.

**Key Features:**
- Attribute validation for `title` and `author`.
- `__eq__` and `__hash__` methods for equality and hashing based on title and author.
- Example showing the use of books as dictionary keys.

### 3. `Shape` Class (`tx4.py`)
Represents a shape with a defined area. Two shapes are considered equal if they have the same area, allowing them to be used as dictionary keys or set elements.

**Key Features:**
- Validation for the area attribute.
- `__eq__` and `__hash__` methods based on area.
- Example usage with dictionary keys for shape descriptions.

### 4. `Transaction` Class (`tx5.py`)
A class to handle transactions, uniquely identified by a `transaction_id`. Transactions with the same ID are treated as duplicates, which is helpful for collections requiring unique entries.

**Key Features:**
- Attribute validation for `transaction_id` and `amount`.
- `__eq__` and `__hash__` methods to ensure transactions are unique by `transaction_id`.
- Example usage in a set to demonstrate uniqueness.

## Getting Started

Clone the repository:
```bash
git clone https://github.com/yourusername/ClassObjects-Python-Examples.git
