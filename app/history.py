import pandas as pd
import os

class CalculationHistory:
    """Manages calculation history using Pandas."""
    HISTORY_FILE = "history.csv"

    def __init__(self):
        """Initialize history storage."""
        if not os.path.exists(self.HISTORY_FILE):
            self._initialize_history()

    def _initialize_history(self):
        """Create a new history file with a header."""
        df = pd.DataFrame(columns=["num1", "num2", "operation", "result"])
        df.to_csv(self.HISTORY_FILE, index=False)

    def add_entry(self, num1, num2, operation, result):
        """Add a new calculation to history."""
        df = pd.read_csv(self.HISTORY_FILE)
        new_entry = pd.DataFrame([[num1, num2, operation, result]], columns=df.columns)
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(self.HISTORY_FILE, index=False)

    def load_history(self):
        """Load calculation history."""
        return pd.read_csv(self.HISTORY_FILE)

    def clear_history(self):
        """Clear all history records."""
        self._initialize_history()
