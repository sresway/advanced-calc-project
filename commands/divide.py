"""Division command for the calculator."""

def execute(num1, num2):
    """Perform division, handling division by zero."""
    if num2 == 0:
        return "Result: Cannot divide by zero"
    return num1 / num2
