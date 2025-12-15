"""
Simple calculator utilities for demonstration purposes.

This module exists to provide executable, well-defined logic that can be
picked up and documented by automated documentation tools such as BMAD.
"""


def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a (int): First operand.
        b (int): Second operand.

    Returns:
        int: The sum of a and b.
    """
    return a + b


def run_example() -> None:
    """
    Execute a simple example calculation and print the result.

    This function serves as a runnable entry point for demonstration
    and documentation purposes.
    """
    result = add(1, 2)
    print(f"Result of 1 + 2 is {result}")


if __name__ == "__main__":
    run_example()
