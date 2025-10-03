import pandas as pd
from src.core.analyzer_engine import AnalyzerEngine
def test_end_to_end():
    df = pd.read_csv("tests/test_data/sample_sales.csv")
    engine = AnalyzerEngine()
    res = engine.analyze(df)
    assert "target" in res and "message" in res
