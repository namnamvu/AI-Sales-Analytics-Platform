import pandas as pd
def corr_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df.corr()
