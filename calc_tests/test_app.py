"""Testing for App"""

import pytest
from app.app import CalculatorApp


@pytest.fixture
def app():
    """Fixture to create a new instance of CalculatorApp for each test."""
    return CalculatorApp()


def test_unknown_command(app):
    """Test handling of unknown commands."""
    result = app.run_command("unknown")
    assert "Invalid command format" in result 


def test_invalid_input(app):
    """Test invalid numeric input handling."""
    result = app.run_command("a b add")
    assert "Invalid number input" in result


def test_repl_menu(app):
    """Test that REPL shows available commands when 'menu' is entered."""
    result = app.run_command("menu")
    assert "Available Commands: add, subtract, multiply, divide" in result


def test_addition(app):
    """Test addition operation."""
    result = app.run_command("5 3 add")
    assert "Result: 8.0" in result


def test_division_by_zero(app):
    """Test division by zero handling."""
    result = app.run_command("5 0 divide")
    assert "Result: Cannot divide by zero" in result 
