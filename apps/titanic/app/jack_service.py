from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score

from titanic.app.walter_reader import WalterReader
from titanic.app.rose_model import RoseModel

_CSV_PATH = Path(__file__).resolve().parent / "Titanic-Dataset.csv"


class JackService:
    def __init__(self):
        self.w = WalterReader()
        self.rose = RoseModel()

    def get_data(self):
        return self.w.get_data()

    def get_count(self):
        return self.w.get_count()

    def get_count_survived(self):
        return self.w.get_count_survived()

    def get_count_dead(self):
        return self.w.get_count_dead()

    def get_training_model_name(self):
        if self.rose.model is None:
            return "No model loaded"
        return type(self.rose.model).__name__

