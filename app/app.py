"""Calculator Application Module"""

import logging
from commands import add, subtract, multiply, divide
from app.history import HistoryManager 

class CalculatorApp:
    """Main calculator application."""

    def __init__(self):
        """Initialize the calculator with available commands and history manager."""
        self.commands = {
            "add": add.execute,
            "subtract": subtract.execute,
            "multiply": multiply.execute,
            "divide": divide.execute,
        }
        self.history = HistoryManager()  

    def run_command(self, command_str):
        """Execute a command if valid. If not, return an error message."""
        try:
            if command_str.lower() == "menu":
                return "Available Commands: add, subtract, multiply, divide, history, clear_history"

            parts = command_str.split()
            if len(parts) != 3:
                return "Invalid command format. Use: <num1> <num2> <operation>"

            # Validate input BEFORE converting
            num1, num2, operation = parts
            if not num1.replace(".", "", 1).isdigit() or not num2.replace(".", "", 1).isdigit():
                return "Invalid number input. Please provide two numbers followed by an operation."

            num1, num2 = float(num1), float(num2)

            if operation not in self.commands:
                return f"Unknown operation: {operation}"

            result = self.commands[operation](num1, num2)

            # Ensure the result is a number before returning
            if isinstance(result, (int, float)):
                formatted_result = f"Result: {result:.1f}"  # Ensures consistent float output
                self.history.save_entry(f"{num1} {operation} {num2}", formatted_result)  # Save operation to history
                return formatted_result
            else:
                return "An unexpected error occurred: Operation did not return a number."

        except ZeroDivisionError:
            return "Result: Cannot divide by zero"
        except Exception as error:
            return f"An unexpected error occurred: {error}"
        
    def view_history(self):
        """Display calculation history."""
        return self.history.load_history()

    def clear_history(self):
        """Clear calculation history."""
        return self.history.clear_history()
