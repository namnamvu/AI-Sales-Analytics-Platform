import pandas as pd

COMMON_TARGETS = {"target","label","y","sales","revenue","amount","profit","gmv","conversion","churn"}

def normalize(col: str) -> str:
    return col.strip().lower().replace(" ", "_")

class TargetDetector:
    def __init__(self):
        pass

    def detect_target(self, df: pd.DataFrame) -> str:
        cols = list(df.columns)
        # 1) name match
        for c in cols:
            if normalize(c) in COMMON_TARGETS:
                return c
        # 2) rightmost numeric with variance
        for c in reversed(cols):
            s = df[c]
            if pd.api.types.is_numeric_dtype(s) and s.nunique() > 5:
                return c
        # 3) fallback to last column
        return cols[-1]
