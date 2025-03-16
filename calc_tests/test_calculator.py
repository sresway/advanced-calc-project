"""Unit tests for the Calculator class."""

from io import StringIO
import sys
from calculator import Calculator

def run_calculator_with_input(monkeypatch, inputs):
    '''Simulates user input and captures output from the calculator.'''
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    captured_output = StringIO()
    sys.stdout = captured_output  # Redirect stdout

    calc = Calculator()  # Create an instance of the calculator

    for command in inputs:
        try:
            parts = command.split()
            operation = parts[0]
            if operation == "add":
                result = calc.add(float(parts[1]), float(parts[2]))
            elif operation == "subtract":
                result = calc.subtract(float(parts[1]), float(parts[2]))
            elif operation == "multiply":
                result = calc.multiply(float(parts[1]), float(parts[2]))
            elif operation == "divide":
                try:
                    result = calc.divide(float(parts[1]), float(parts[2]))
                except ValueError as e:
                    result = str(e)
            elif operation == "history":
                result = "History:\n" + "\n".join(calc.get_history())
            elif operation == "clear_history":
                calc.clear_history()
                result = "History cleared"
            else:
                result = "Unknown operation"

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input")

    sys.stdout = sys.__stdout__
    return captured_output.getvalue()
