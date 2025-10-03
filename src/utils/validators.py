import pandas as pd
from typing import List

def validate_csv_df(df: pd.DataFrame) -> List[str]:
    issues = []
    if df.empty:
        issues.append("Empty dataframe")
    if df.shape[0] < 5:
        issues.append("Less than 5 rows: results may be unstable")
    for c in df.columns:
        if c.strip()=="" or c is None:
            issues.append("Found empty column name")
    return issues
