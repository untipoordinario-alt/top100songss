import pandas as pd

def limpiar_dataframe(df):
    if "_id" in df.columns:
        df = df.drop(columns=["_id"])
    return df
