import pickle
from pathlib import Path

import joblib
from sklearn.tree import DecisionTreeClassifier

_DATA_DIR = Path(__file__).resolve().parent
_JOBLIB_PATH = _DATA_DIR / "titanic_decision_tree.joblib"
_PKL_PATH = _DATA_DIR / "titanic_decision_tree.pkl"

_MODEL_PATH = _JOBLIB_PATH

# 이 모듈이 기대하는 학습 모델 타입 (이름 문자열은 항상 sklearn 트리 클래스명과 동일)
MODEL_CLASS_NAME = DecisionTreeClassifier.__name__


class RoseModel:
    def __init__(self) -> None:
        self.model = DecisionTreeClassifier()

    def get_model_name(self):
        return type(self.model).__name__