"""Command Plugins"""

import importlib
import os

def load_plugins():
    """Dynamically load commands as plugins."""
    plugins = {}
    commands_path = os.path.join(os.path.dirname(__file__), "..", "commands")
    
    for filename in os.listdir(commands_path):
        if filename.endswith(".py") and filename != "__init__.py":
            command_name = filename[:-3]  # Remove ".py" extension
            module_name = f"commands.{command_name}"
            
            try:
                module = importlib.import_module(module_name)
                if hasattr(module, "execute"):
                    plugins[command_name] = module.execute
            except Exception as e:
                print(f"Error loading {module_name}: {e}")

    return plugins
