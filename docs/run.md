# run.py

Convenience runner script that executes the `helloworld` package as a standalone application.

## Purpose

This script serves as the main entry point for running the hello world package without requiring package installation. It dynamically adds the `src` directory to Python's module search path and executes the `helloworld` module.

## Behavior

- Resolves the script's parent directory and adds `src/` to `sys.path`
- Uses `runpy.run_module()` to execute the `helloworld` package as `__main__`
- Preserves command-line arguments and exit codes from the target module

## Usage

Execute directly from the repository root:

```bash
python3 run.py
```

Or make executable and run:

```bash
chmod +x run.py
./run.py
```

## Requirements

- The `src/helloworld/` directory must exist relative to this script
- The `helloworld` package must be properly structured with `__main__.py` or equivalent entry point