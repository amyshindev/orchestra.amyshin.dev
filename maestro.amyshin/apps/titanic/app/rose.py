import pickle
from pathlib import Path

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"
_MODEL_PATH = _DATA_DIR / "titanic_decision_tree.pkl"


class Rose:
    def __init__(self):
        pass

    def save_decision_tree_model(self):
        df = pd.read_csv(_CSV_PATH)

        feature_cols = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
        X = df[feature_cols].copy()
        y = df["Survived"].astype(int)

        numeric_cols = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
        categorical_cols = ["Sex", "Embarked"]

        for col in numeric_cols:
            X[col] = X[col].fillna(X[col].median())
        for col in categorical_cols:
            X[col] = X[col].fillna("Unknown")

        X = pd.get_dummies(X, columns=categorical_cols, drop_first=False)

        model = DecisionTreeClassifier(random_state=42, max_depth=5)
        model.fit(X, y)

        artifact = {
            "model": model,
            "feature_columns": list(X.columns),
        }

        with open(_MODEL_PATH, "wb") as f:
            pickle.dump(artifact, f)

        return str(_MODEL_PATH)