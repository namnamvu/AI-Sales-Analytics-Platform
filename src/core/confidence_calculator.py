def model_confidence_from_metric(metric_name: str, value: float) -> float:
    if value is None:
        return 0.0
    return max(0.0, min(1.0, float(value)))
