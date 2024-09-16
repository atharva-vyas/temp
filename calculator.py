# T
import math

def add(x, y):
    """Addition"""
    return x + y

def subtract(x, y):
    """Subtraction"""
    return x - y

def multiply(x, y):
    """Multiplication"""
    return x * y

def divide(x, y):
    """Division"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


def sqrt(x):
    if x < 0:
        raise ValueError("Square root of negative number is not defined in the real number system.")
    else:
        return math.sqrt(x)

# Change made by Faisal Ahmad:

def power(x, y):
    return x**y

