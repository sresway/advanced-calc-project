"""Division command for the calculator."""

def execute(num1, num2):
    """Perform division"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        raise ValueError("Result: Cannot divide by zero")
