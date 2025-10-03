import os
RANDOM_STATE = int(os.getenv("RANDOM_STATE","42"))
ENABLE_SHAP = os.getenv("ENABLE_SHAP","true").lower() in ("1","true","yes")
MAX_ROWS = int(os.getenv("MAX_ROWS","200000"))
CV_FOLDS = int(os.getenv("CV_FOLDS","5"))
