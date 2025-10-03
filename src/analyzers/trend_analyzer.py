# Lightweight trend detection stub
import pandas as pd

def detect_trend(ts: pd.Series) -> dict:
    try:
        x = pd.Series(range(len(ts)))
        y = ts.fillna(ts.mean()).astype(float)
        coef = ((x - x.mean())*(y - y.mean())).sum() / (((x - x.mean())**2).sum() + 1e-9)
        return {"slope": float(coef)}
    except Exception:
        return {"slope": 0.0}
