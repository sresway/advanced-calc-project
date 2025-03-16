"""Testing Main.py"""

import os
import pytest
import subprocess
import logging

# Override environment variable to prevent extra output
os.environ["ENVIRONMENT"] = "test"

# Configure logging for testing
logging.basicConfig(
    filename="test_log.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

@pytest.mark.parametrize(
    "args, expected_output",
    [
        (["5", "3", "add"], "Result: 8"),
        (["10", "2", "subtract"], "Result: 8"),
        (["4", "5", "multiply"], "Result: 20"),
        (["20", "4", "divide"], "Result: 5"),
        (["1", "0", "divide"], "Result: Cannot divide by zero"),
        (["9", "3", "unknown"], "Unknown operation: unknown"),
        (["a", "3", "add"], "Invalid number input. Please provide two numbers followed by an operation."),
        (["5", "b", "subtract"], "Invalid number input. Please provide two numbers followed by an operation."),
    ]
)
def test_main(args, expected_output):
    """Test command-line input for the calculator program."""
    result = subprocess.run(
        ["python", "main.py"] + args,
        capture_output=True,
        text=True,
        check=False
    )

    # Debug output
    print("STDOUT:", result.stdout.strip())
    print("STDERR:", result.stderr.strip())

    # Logging
    logging.info("Testing: python main.py %s", " ".join(args))
    logging.info("Expected Output: %s", expected_output)
    logging.info("Actual Output: %s", result.stdout.strip())
    logging.info("Errors: %s", result.stderr.strip())

    # Check if expected output is in stdout
    assert expected_output in result.stdout.strip(), (
        f"\n Expected: '{expected_output}'\n"
        f" Got: '{result.stdout.strip()}'"
    )
