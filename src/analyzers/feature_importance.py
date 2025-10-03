from typing import Dict
import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_regression, mutual_info_classif

class FeatureImportanceAnalyzer:
    def __init__(self, random_state: int = 42):
        self.random_state = random_state

    def calculate_importance(self, X: pd.DataFrame, y: pd.Series) -> Dict[str, float]:
        X_enc = pd.get_dummies(X, drop_first=False)
        try:
            if y.dtype.kind in "fi" and y.nunique() > 10:
                mi = mutual_info_regression(X_enc.fillna(0), y.fillna(y.mean()), random_state=self.random_state)
            else:
                mi = mutual_info_classif(X_enc.fillna(0), y.fillna(method="ffill"), random_state=self.random_state)
            scores = dict(zip(X_enc.columns.tolist(), mi))
            total = sum(scores.values()) or 1.0
            norm = {k: float(v)/total for k,v in scores.items()}
            return norm
        except Exception:
            scores = {c: float(X[c].std()) if X[c].dtype.kind in "fi" else 0.0 for c in X.columns}
            total = sum(scores.values()) or 1.0
            return {k: v/total for k,v in scores.items()}
