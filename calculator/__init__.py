""" This module defines the Calculator class with basic arithmetic operations."""
class Calculator:
    """Create calculator class"""
    _history = []

    @staticmethod
    def add(a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        result = a + b
        Calculator._history.append(f"{a} + {b} = {result}")
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Returns the difference of two numbers."""
        result = a - b
        Calculator._history.append(f"{a} - {b} = {result}")
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Returns the product of two numbers."""
        result = a * b
        Calculator._history.append(f"{a} * {b} = {result}")
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Returns the quotient of two numbers."""
        if b == 0:
            raise ValueError("Result: Cannot divide by zero")
        result = a / b
        Calculator._history.append(f"{a} / {b} = {result}")
        return result

    @classmethod
    def get_history(cls):
        """Returns history"""
        return cls._history

    @classmethod
    def clear_history(cls):
        """Clears history."""
        cls._history.clear()
