import pandas as pd
from src.core.data_processor import DataProcessor
def test_process_basic():
    df = pd.DataFrame({"a":[1,2,2],"b":[3,4,5]})
    dp = DataProcessor()
    out = dp.process(df)
    assert "a" in out.columns
