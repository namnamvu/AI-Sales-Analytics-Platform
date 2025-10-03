from typing import Dict, Any
import pandas as pd
from ..detectors.target_detector import TargetDetector
from ..analyzers.feature_importance import FeatureImportanceAnalyzer
from ..explainers.natural_language import NaturalLanguageExplainer
from ..core.data_processor import DataProcessor

class AnalyzerEngine:
    def __init__(self):
        self.dt = DataProcessor()
        self.target_detector = TargetDetector()
        self.feature_analyzer = FeatureImportanceAnalyzer()
        self.explainer = NaturalLanguageExplainer()

    def analyze(self, df: pd.DataFrame) -> Dict[str, Any]:
        df = self.dt.process(df)
        target = self.target_detector.detect_target(df)
        X = df.drop(columns=[target])
        y = df[target]
        importance = self.feature_analyzer.calculate_importance(X, y)
        text = self.explainer.feature_to_text(target, importance)
        return {"target": target, "drivers": importance, "message": text["message"], "top_drivers": text["drivers"]}
