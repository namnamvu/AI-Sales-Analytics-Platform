# Minimal anomaly detector stub - flags extreme z-scores
import numpy as np
import pandas as pd

def simple_anomaly_flags(df: pd.DataFrame, z_thresh: float = 3.0) -> dict:
    flags = {}
    for c in df.select_dtypes(include=[float,int]).columns:
        col = df[c].astype(float)
        z = (col - col.mean()) / (col.std() + 1e-9)
        flags[c] = int((z.abs() > z_thresh).sum() > 0)
    return flags
