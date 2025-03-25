"""Calculator Application Module"""

import logging
from app.history import HistoryManager
from app.plugins import load_plugins

class CalculatorApp:
    """Main calculator application."""

    def __init__(self):
        """Initialize the calculator with available commands and history manager."""
        self.history_manager = HistoryManager()
        self.commands = load_plugins()

        self.commands["history"] = self.view_history
        self.commands["clear_history"] = self.clear_history

    def run_command(self, command_str):
        """Execute a command if valid. If not, return an error message."""
        try:
            command = command_str.lower()

            if command == "menu":
                return "Available Commands: " + ", ".join(self.commands.keys())

            if command in ["history", "clear_history"]:
                return self.commands[command]() 

            parts = command_str.split()
            if len(parts) != 3:
                return "Invalid command format. Use: <num1> <num2> <operation>"

            num1, num2, operation = parts
            num1, num2 = float(num1), float(num2)

            if operation not in self.commands:
                return f"Unknown operation: {operation}"

            result = self.commands[operation](num1, num2)

            if isinstance(result, (int, float)):
                formatted = f"Result: {int(result)}" if result.is_integer() else f"Result: {result}"
                self.history_manager.save_entry(f"{num1} {operation} {num2}", result)
                return formatted
            else:
                return f"An unexpected error occurred: Operation did not return a number."

        except ZeroDivisionError:
            return "Result: Cannot divide by zero"
        except ValueError:
            return "Invalid number input. Please provide two numbers followed by an operation."
        except Exception as error:
            logging.error("Unhandled exception: %s", error)
            return f"An unexpected error occurred: {error}"

    def view_history(self):
        """Return string of history or message if empty."""
        df = self.history_manager.load_history()
        if df.empty:
            return "No history found."
        return df.to_string(index=False)

    def clear_history(self):
        """Clear history file."""
        self.history_manager.clear_history()
        return "History cleared."
