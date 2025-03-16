"""Menu command for listing available operations."""

import pkgutil
import commands


def execute():
    """Dynamically lists all available commands."""
    command_list = [name for _, name, _ in pkgutil.iter_modules(commands.__path__)]
    return f"Available Commands: {', '.join(command_list)}"
