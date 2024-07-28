#12. Write a Python module named calculator.py containing functions for addition, subtraction, multiplication, and division.

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference between a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
