"""Configuration file for pytest test setup."""

import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    """Add command-line argument for number of test cases."""
    print("\n✅ pytest_addoption LOADED in conftest.py\n")  # DEBUG LOG
    parser.addoption(
        "--num_records",
        action="store",
        default=10,
        type=int,
        help="Number of test records to generate."
    )

@pytest.fixture
def get_num_records(request):
    """Retrieve the # of records requested via pytest"""
    print("\n✅ num_records fixture LOADED in conftest.py\n")  # DEBUG LOG
    return request.config.getoption("--num_records")

def generate_test_cases(n):
    """Generate dynamic test cases using Faker."""
    test_cases = []
    for _ in range(n):
        a = fake.random_int(min=1, max=100)
        b = fake.random_int(min=1, max=100)
        operation = fake.random_element(elements=["add", "subtract", "multiply", "divide"])
        expected = None
        if operation == "add":
            expected = a + b
        elif operation == "subtract":
            expected = a - b
        elif operation == "multiply":
            expected = a * b
        elif operation == "divide":
            expected = a / b if b != 0 else "Cannot divide by zero"
        test_cases.append((a, b, operation, expected))
    return test_cases

def pytest_generate_tests(metafunc):
    """Parameterize test cases based on --num_records."""
    print("pytest_generate_tests LOADED in conftest.py\n")  # DEBUG LOG
    if "num_records" in metafunc.config.option:  # Ensure option exists
        num_tests = metafunc.config.option.num_records
        if {"a", "b", "operation", "expected"}.issubset(metafunc.fixturenames):
            test_cases = generate_test_cases(num_tests)
            metafunc.parametrize("a, b, operation, expected", test_cases)
