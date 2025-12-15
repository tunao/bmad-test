#!/usr/bin/env python3
"""
Convenience runner for the hello world package.

This script serves as the main entry point for running the `helloworld` module.
It also demonstrates a simple computation that can be documented by BMAD.
"""
import runpy


def calculate_example_sum() -> int:
    """
    Calculate a simple example sum.

    This function exists mainly to demonstrate how small utility logic
    can be documented and traced by automated documentation tools (BMAD).

    Returns:
        int: The result of 1 + 2.
    """
    return 1 + 2


if __name__ == "__main__":
    result = calculate_example_sum()
    print(f"1 + 3 = {result}")

    runpy.run_module("helloworld", run_name="__main__")
