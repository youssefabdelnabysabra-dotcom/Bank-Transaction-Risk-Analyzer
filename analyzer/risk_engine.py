import numpy as np
from scipy.stats import zscore




class FeatureBuilder:
    def build_features(self, df):
        df = df.copy()

        df["day"] = df["step"] // 24
        df["transaction_count"] = df.groupby("nameOrig")["nameOrig"].transform("count")
        df["total_amount"] = df.groupby("nameOrig")["amount"].transform("sum")
        df["avg_amount"] = df.groupby("nameOrig")["amount"].transform("mean")
        df["max_amount"] = df.groupby("nameOrig")["amount"].transform("max")
        df["daily_velocity"] = (
            df.groupby(["nameOrig", "day"])
            .transform("size")
        )

        df["rolling_avg_amount"] = (
            df.groupby("nameOrig")["amount"]
              .rolling(window=3, min_periods=1)
              .mean()
              .reset_index(level=0, drop=True)
        )

        df["balance_error"] = abs(
            (df["oldbalanceOrg"] - df["newbalanceOrig"]) - df["amount"]
        )
        print("Features built successfully.")
        return df

class RiskScorer:
    def score(self, df):
        df = df.copy()

        df["amount_zscore"] = zscore(df["amount"])

        def classify(z):
            z = abs(z)
            if z < 1:
                return "Low"
            elif z < 2:
                return "Medium"
            elif z < 3:
                return "High"
            else:
                return "Critical"

        df["risk_level"] = df["amount_zscore"].apply(classify)
        print("risk scoring completed.")
        return df



class TransactionFlagger:
    def flag(self, df):
        df = df.copy()

        df["is_suspicious"] = np.where(
            (df["type"].isin(["TRANSFER", "CASH_OUT"])) &
            (df["newbalanceOrig"] == 0) &
            (df["oldbalanceOrg"] > 0) &
            (df["balance_error"] > 1),
            1,
            0
        )
        
        print(f"suspicious transactions found: {df['is_suspicious'].sum()}")
        return df

