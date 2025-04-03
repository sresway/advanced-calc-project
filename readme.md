Video Link:

[https://youtu.be/j59KU_HPEnc
](https://youtu.be/j59KU_HPEnc)

Project Details: 

For this calculator project, I implemented a few key design patterns to help keep the code organized, expandable, and easier to maintain:

Command Pattern: Each operation like add, subtract, divide, etc., is treated as a command with its own execute() method. This makes it easy to add or update operations later without modifying core logic.
        - You can see this in the commands folder – each file defines a consistent interface for executing operations.

Plugin Pattern: I used a plugin loader (plugins.py) to load all available operations at runtime. This keeps the calculator flexible and allows new functionality to be added without changing the main app. This implementation dynamically imports modules from the commands directory.
I used environment variables to control behavior between development and test environments.

For example, the app checks the environment before printing setup messages or loading logs. This helps prevent test output from being cluttered.
        - This is handled in main.py using dotenv and a .env file like:
        ENVIRONMENT=development

Logging was added throughout the app to help debug and monitor what’s happening. Logs record when commands are run, errors occur, or plugins fail to load. They go to both the console and a calculator.log file.
        - Logging is set up in main.py using Python’s built-in logging module with a custom format (timestamp, log level, and the message.) and log to multiple places at once.

I used EAFP (Easier to Ask for Forgiveness than Permission) in many places.
    - Rather than checking if inputs are valid ahead of time, the app tries to convert values to float and catches ValueError if something goes wrong.
    - There's also a specific ZeroDivisionError block to gracefully catch division by zero attempts.
        - This logic is all in CalculatorApp.run_command() in app/app.py.

## QR Code to My GitHub

![QR Code][def]


[def]: qr_codes/my_github_qr.png