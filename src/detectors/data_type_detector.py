import pandas as pd

def detect_types(df: pd.DataFrame) -> dict:
    types = {}
    for c in df.columns:
        types[c] = str(df[c].dtype)
    return types
