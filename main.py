"""Main entry point for the calculator program (Command-Line Mode)."""

import os
import sys
import logging
from dotenv import load_dotenv
from app.app import CalculatorApp

# Load environment variables
load_dotenv()

# Override ENVIRONMENT to "test" when running tests
ENV = os.getenv("ENVIRONMENT", "development")

# Prevent environment message from appearing in test runs
if ENV != "test":
    print(f"Environment: {ENV}")

# Configure Logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("calculator.log"),  # Save logs to a file
        logging.StreamHandler(),  # Print logs to console
    ]
)

def main():
    """Run the calculator as a command-line tool."""
    calc = CalculatorApp()

    if len(sys.argv) > 1:
        command = " ".join(sys.argv[1:])
        print(calc.run_command(command))
        sys.exit(0)  # ✅ Exit cleanly after command execution

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == "exit":
                print("Exiting calculator...")
                sys.exit(0)
            print(calc.run_command(user_input))
        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Exiting...")
            sys.exit(0)

if __name__ == "__main__":
    main()