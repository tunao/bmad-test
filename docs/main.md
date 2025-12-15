# main.py

## Overview

Convenience runner script that demonstrates basic arithmetic and executes the `helloworld` module. This file serves as an entry point for running the hello world package with additional demonstration code.

## Functionality

When executed directly, this script:
1. Performs a simple arithmetic calculation (1 + 2)
2. Prints the result to stdout
3. Executes the `helloworld` module using `runpy.run_module()`

## Public API

This file has no public functions or classes - it is designed to be executed as a script.

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

## Invariants

- The script will always print "1 + 2 = 3" before executing the helloworld module
- Requires the `helloworld` module to be importable, otherwise `runpy.run_module()` will raise `ModuleNotFoundError`