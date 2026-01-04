import pandas as pd
import numpy as np


class DataManager:
    require_colums = {
        "step", "type", "amount",
        "nameOrig", "oldbalanceOrg", "newbalanceOrig",
        "nameDest", "oldbalanceDest", "newbalanceDest",
        "isFraud"
    }

    def load_data(self, file_path, nrows=None):
        df = pd.read_csv(file_path, nrows=nrows)

        missing = self.require_colums - set(df.columns)
        if missing:
            raise ValueError(f"missing requir colums   {missing}")
        print("dataset load successfully")
        return df

class Cleaner:
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        numeric_cols = df.select_dtypes(include=np.number).columns
        df[numeric_cols] = df[numeric_cols].fillna(0)

        categorical_cols = df.select_dtypes(exclude=np.number).columns
        df[categorical_cols] = df[categorical_cols].fillna("UNKNOWN")

        df = df[df["amount"] >= 0]
        df = df[df["oldbalanceOrg"] >= 0]
        df = df[df["newbalanceOrig"] >= 0]
        df = df[df["oldbalanceDest"] >= 0]
        df = df[df["newbalanceDest"] >= 0]
        df.drop_duplicates(inplace=True)

        print("data cleaned")
        return df
 
 
 
 