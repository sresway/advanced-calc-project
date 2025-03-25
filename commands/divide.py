"""Division command for the calculator."""

def execute(num1, num2):
    """Perform division"""
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2
