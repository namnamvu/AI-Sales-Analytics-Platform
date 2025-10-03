# src/explainers/natural_language.py
from typing import Dict, Any, List

class NaturalLanguageExplainer:
    """
    Turns model outputs into human-readable business insights.
    """

    def explain(self, target: str, importance: Dict[str, float]) -> Dict[str, Any]:
        sorted_feats = sorted(importance.items(), key=lambda x: -x[1])
        top3 = sorted_feats[:3]
        message = (
            f"Your {target} is primarily driven by "
            + ", ".join([f[0] for f in top3])
            + "."
        )
        drivers = [{"feature": f, "score": round(s, 3)} for f, s in top3]
        return {"target": target, "message": message, "drivers": drivers}

    def feature_to_text(self, target:str, importance:Dict[str,float]) -> Dict[str,Any]:
        sorted_feats = sorted(importance.items(), key=lambda x: -x[1])
        top3 = sorted_feats[:3]
        message = f"Your {target} is primarily driven by " + ", ".join([f[0] for f in top3]) + "."
        drivers = [{"feature": f, "score": round(s,3)} for f,s in top3]
        return {"target": target, "message": message, "drivers": drivers}