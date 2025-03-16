"""History Management for Calculator"""

import pandas as pd

class HistoryManager:
    """Manages calculation history using Pandas"""

    def __init__(self, history_file="history.csv"):
        self.history_file = history_file
        try:
            self.history = pd.read_csv(self.history_file)
        except FileNotFoundError:
            self.history = pd.DataFrame(columns=["Operation", "Result"])

    def save_entry(self, operation, result):
        """Save a calculation to history"""
        new_entry = pd.DataFrame([{"Operation": operation, "Result": result}])
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.history.to_csv(self.history_file, index=False)

    def load_history(self):
        """Return all saved calculations as a DataFrame"""
        if self.history.empty:
            return pd.DataFrame(columns=["Operation", "Result"])
        return self.history

    def clear_history(self):
        """Clear all calculation history"""
        self.history = pd.DataFrame(columns=["Operation", "Result"])
        self.history.to_csv(self.history_file, index=False)
