# Basic k-means segmentation stub (requires scikit-learn)
import pandas as pd
from sklearn.cluster import KMeans

def auto_segment(df: pd.DataFrame, k:int=3):
    num = df.select_dtypes(include=["number"]).fillna(0)
    if num.shape[0] < k:
        return [0]*num.shape[0]
    kmeans = KMeans(n_clusters=k, random_state=42).fit(num)
    return kmeans.labels_.tolist()
