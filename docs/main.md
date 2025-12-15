# main.py

## Overview

Convenience runner script that demonstrates basic arithmetic and executes the `helloworld` module. This file serves as an entry point for running the hello world package with additional demonstration code for automated documentation tools (BMAD).

## Functions

### calculate_example_sum() -> int

Calculate a simple example sum.

This function exists mainly to demonstrate how small utility logic can be documented and traced by automated documentation tools (BMAD).

**Returns:**
- `int`: The result of 1 + 2 (always returns 3)

## Functionality

When executed directly, this script:
1. Calls `calculate_example_sum()` to perform arithmetic calculation
2. Prints the result to stdout
3. Executes the `helloworld` module using `runpy.run_module()`

## Public API

### Functions
- `calculate_example_sum()` - Returns the sum of 1 + 2

## Dependencies

- `runpy` (standard library) - used to execute the helloworld module
- `helloworld` module - must be available in the Python path

## Usage Examples

### Direct execution
```bash
python3 main.py
```

### Expected output
```
1 + 2 = 3
[output from helloworld module]
```

### Using the function programmatically
```python
from main import calculate_example_sum
result = calculate_example_sum()  # returns 3
```

## Invariants

- `calculate_example_sum()` will always return 3
- The script will always print "1 + 2 = 3" before executing the helloworld module
- Requires the `helloworld` module to be importable, otherwise `runpy.run_module()` will raise `ModuleNotFoundError`