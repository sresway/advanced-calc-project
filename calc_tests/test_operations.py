"""Testing for the Calculator class."""

import pytest
from faker import Faker
from calculator import Calculator

fake = Faker()

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 3.5, 6.0),
        (-2.5, 3.5, 1.0),
    ]
)
def test_addition(a: float, b: float, expected: float):
    """Test the addition operation."""
    result = Calculator.add(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (fake.random_int(min=1, max=100), fake.random_int(min=1, max=100), None),
        (fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        fake.pyfloat(left_digits=2, right_digits=2, positive=True), None),
    ]
)
def test_addition_faker(a: float, b: float, expected):
    """Test the addition operation with random numbers from Faker."""
    expected = a + b
    result = Calculator.add(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (-5, -3, -2),
        (10.5, 5.5, 5.0),
        (-10.5, -5.5, -5.0),
    ]
)
def test_subtraction(a: float, b: float, expected: float):
    """Test the subtraction operation."""
    result = Calculator.subtract(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (fake.random_int(min=1, max=100), fake.random_int(min=1, max=100), None),
        (fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        fake.pyfloat(left_digits=2, right_digits=2, positive=True), None),
    ]
)
def test_subtraction_faker(a: float, b: float, expected):
    """Test the subtraction operation with random numbers from Faker."""
    expected = a - b
    result = Calculator.subtract(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 10, 0),
        (-2, -3, 6),
        (2.5, 4.0, 10.0),
        (-2.5, 4.0, -10.0),
    ]
)
def test_multiplication(a: float, b: float, expected: float):
    """Test the multiplication operation."""
    result = Calculator.multiply(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (fake.random_int(min=1, max=100), fake.random_int(min=1, max=100), None),
        (fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        fake.pyfloat(left_digits=2, right_digits=2, positive=True), None),
    ]
)
def test_multiplication_faker(a: float, b: float, expected):
    """Test the multiplication operation with random numbers from Faker."""
    expected = a * b
    result = Calculator.multiply(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),
        (-6, -3, 2.0),
        (6.0, 3.0, 2.0),
        (-6.0, 3.0, -2.0),
        (0, 5, 0.0),
    ]
)
def test_division(a: float, b: float, expected: float):
    """Test the division operation."""
    result = Calculator.divide(a, b)
    assert result == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
       (fake.random_int(min=1, max=100), fake.random_int(min=1, max=100), None),
        (fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        fake.pyfloat(left_digits=2, right_digits=2, positive=True), None),
    ]
)
def test_division_faker(a: float, b: float, expected):
    """Test the division operation with random numbers from Faker."""
    expected = a / b
    result = Calculator.divide(a, b)
    assert result == expected
