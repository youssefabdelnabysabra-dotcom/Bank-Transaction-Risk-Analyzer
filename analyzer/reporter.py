import os


class ReportGenerator:
    def generate(self, df, output_dir="reports"):
        os.makedirs(output_dir, exist_ok=True)

        flaged = df[df["is_suspicious"] == 1]
        flaged.to_csv(f"{output_dir}/flaged_transctions.csv", index=False)

        customer_summary = (
            df.groupby("nameOrig")
            .agg(
                total_transactions=("amount", "count"),
                total_amount=("amount", "sum"),
                avg_amount=("amount", "mean"),
                max_amount=("amount", "max"),
                critical_risks=("risk_level", lambda x: (x == "Critical").sum()),
                suspicious_tx=("is_suspicious", "sum")
            )
            .reset_index()
            .sort_values("critical_risks", ascending=False)
        )

        customer_summary.to_csv(
            f"{output_dir}/customer_risk_summary.csv", index=False
        )

        with open(f"{output_dir}/report.txt", "w") as f:
            f.write("BANK TRANSACTION RISK REPORT\n")
            f.write("=" * 40 + "\n\n")
            f.write(f"Total transactions   {len(df)}\n")
            f.write(f"Suspicious transactions  {len(flaged)}\n\n")
            f.write("Top Risky Customers  \n")
            f.write(customer_summary.head(5).to_string(index=False))

        print("reports generated successfully")
