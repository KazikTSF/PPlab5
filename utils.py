"""
Utility functions for basic arithmetic operations.
"""


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Divide two numbers."""
    return a / b


def int_to_binary(number: int) -> str:
    """Convert natural number from 0 to 100 to binary string."""
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Number must be a natural number without a decimal part.")
    if number < 0 or number > 100:
        raise ValueError("Number out of range (0-100).")

    return bin(number)[2:]
