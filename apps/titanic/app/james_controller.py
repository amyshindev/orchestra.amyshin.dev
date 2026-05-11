from fastapi import FastAPI


try:
    from .walter_reader import WalterReader
except ImportError:
    from walter_reader import WalterReader

try:
    from .rose_model import model_file_exists
except ImportError:
    from rose_model import model_file_exists

try:
    from .jack_service import JackService
except ImportError:
    from jack_service import JackService


app = FastAPI(title="Titanic (James)")


class JamesController:
    def __init__(self):
        self.jack = JackService()

    def has_decision_tree_model(self):
        """저장된 결정트리 모델 파일 존재 여부 반환."""
        return model_file_exists()

    def get_training_model_name(self):
        return self.jack.get_training_model_name()