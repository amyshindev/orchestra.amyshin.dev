from fastapi import FastAPI


try:
    from .walter import Walter
except ImportError:
    from walter import Walter

try:
    from .rose import _MODEL_PATH
except ImportError:
    from rose import _MODEL_PATH


app = FastAPI(title="Titanic (James)")


class James:
    def __init__(self):
        pass
    
    def get_data(self):
        w = Walter()
        return w.get_data()

    def get_count(self):
        w = Walter()
        return w.get_count()

    def get_count_survived(self):
        w = Walter()
        return w.get_count_survived()

    def get_count_dead(self):
        w = Walter()
        return w.get_count_dead()

    def has_decision_tree_model(self):
        return _MODEL_PATH.exists()