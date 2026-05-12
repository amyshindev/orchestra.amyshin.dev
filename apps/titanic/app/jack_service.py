from titanic.app.rose_model import RoseModel, model_file_exists
from titanic.app.walter_reader import WalterReader


class JackService:
    def __init__(self) -> None:
        self.walter = WalterReader()
        self.rose = RoseModel()

    def get_data(self):
        return self.walter.get_data()

    def get_count(self):
        return self.walter.get_count()

    def has_decision_tree_model(self) -> bool:
        return model_file_exists()

    def get_model_name_and_accuracy(self):
        return self.rose.get_model_name()