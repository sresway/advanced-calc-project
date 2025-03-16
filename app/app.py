"""Calculator Application Module"""

from calculator import Calculator
from commands import add, subtract, multiply, divide

class CalculatorApp:
    """Main calculator application."""

    def __init__(self):
        """Initialize the calculator with available operations."""
        self.calculator = Calculator()  #  Uses Calculator for actual math

    def __init__(self):
        """Initialize the calculator with available commands."""
        self.commands = {
            "add": add.execute,
            "subtract": subtract.execute,
            "multiply": multiply.execute,
            "divide": divide.execute,
        }

    def run_command(self, command_str):
        """Execute a command if valid. If not, return an error message."""
        try:
            if command_str.lower() == "menu":
                return "Available Commands: add, subtract, multiply, divide"

            parts = command_str.split()
            if len(parts) != 3:
                return "Invalid command format. Use: <num1> <num2> <operation>"

            num1, num2, operation = parts
            num1, num2 = float(num1), float(num2)

            if operation not in self.commands:
                return f"Unknown operation: {operation}"

            result = self.commands[operation](num1, num2)

            # ✅ Ensure the result is a valid number before formatting
            if isinstance(result, (int, float)):
                return f"Result: {int(result)}" if result.is_integer() else f"Result: {result}"
            else:
                return "An unexpected error occurred: Operation did not return a number."

        except ValueError:
            return "Invalid number input. Please provide two numbers followed by an operation."

        except ZeroDivisionError:
            return "Result: Cannot divide by zero"

        except Exception as error:
            return f"An unexpected error occurred: {error}"
