# Minimal AutoML stub - choose simple baseline
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

def baseline_model(problem_type:str):
    if problem_type=="regression":
        return RandomForestRegressor(n_estimators=100, random_state=42)
    return RandomForestClassifier(n_estimators=100, random_state=42)
