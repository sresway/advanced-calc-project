""""Configuration file for pytest test setup."""

import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    """Add command-line argument for number of test cases."""
    print("\npytest_addoption LOADED in conftest.py\n")  # DEBUG LOG
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
    print("\nnum_records fixture LOADED in conftest.py\n")  # DEBUG LOG
    return request.config.getoption("--num_records")

    if {"a", "b", "operation", "expected"}.issubset(metafunc.fixturenames):
        test_cases = generate_test_cases(num_tests)
        metafunc.parametrize("a, b, operation, expected", test_cases)
