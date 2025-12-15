# Calculator Module

A simple calculator utility module providing basic arithmetic operations for demonstration and documentation purposes.

## Overview

The `calculator.py` module contains well-defined, executable logic designed to showcase automated documentation capabilities. It provides a basic addition function along with a demonstration entry point.

## Public API

### Functions

#### `add(a: int, b: int) -> int`

Adds two integers and returns their sum.

**Parameters:**
- `a` (int): First operand
- `b` (int): Second operand

**Returns:**
- int: The sum of a and b

**Example:**
```python
result = add(5, 3)  # Returns 8
```

#### `run_example() -> None`

Executes a simple example calculation and prints the result to demonstrate the module's functionality.

This function serves as a runnable entry point for demonstration and documentation purposes, performing a basic addition operation (1 + 2) and displaying the result.

**Example:**
```python
run_example()  # Prints: "Result of 1 + 2 is 3"
```

## Usage

The module can be executed directly as a script:

```bash
python calculator.py
```

This will run the example calculation and display the result.

Alternatively, import and use the functions programmatically:

```python
from calculator import add

result = add(10, 20)
print(f"The sum is {result}")
```

## Module Purpose

This module exists primarily to provide executable, well-defined logic that can be picked up and documented by automated documentation tools such as BMAD. It demonstrates best practices for Python module documentation and API design.
