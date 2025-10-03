import pandas as pd
from ..utils.validators import validate_csv_df
# Cleaning the data
class DataProcessor:
    #Convert csv into structred format
    def __init__(self):
        pass

    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        # normalize columns
        df = df.copy()
        df.columns = [c.strip() for c in df.columns]
        # basic drop duplicates
        df = df.drop_duplicates()
        # drop all-NA cols
        df = df.dropna(axis=1, how="all")
        # validator warnings (not fatal)
        issues = validate_csv_df(df)
        return df
