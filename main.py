from analyzer.data_handler import DataManager, Cleaner
from analyzer.risk_engine import FeatureBuilder, RiskScorer, TransactionFlagger
from analyzer.reporter import ReportGenerator

class ConsoleApp:
    def __init__(self):
        self.data_manager = DataManager()
        self.cleaner = Cleaner()
        self.feature_builder = FeatureBuilder()
        self.risk_scorer = RiskScorer()
        self.flagger = TransactionFlagger()
        self.reporter = ReportGenerator()
        self.df = None

    def run(self):
        while True:
            print("\n Bank transaction Risk and anomaly analyzer;")
            print("1- load dataset")
            print("2- clean and validate data")
            print("3- build features")
            print("4- score transactions")
            print("5- flag suspicious transactions")
            print("6- export reports")
            print("7- display summary")
            print("0- exit")
            choice = input("choose option  ")

            try:
                if choice == "1":
                    path = input("enter dataset file path: ")

                    rows_input = input("number of rows (ppress Enter for all): ").strip()

                    try:
                        rows = int(rows_input) if rows_input else None
                    except ValueError:
                        print("please enter a valid number")
                        continue

                    self.df = self.data_manager.load_data(path, rows)


                elif choice == "2":
                    self._require_data()
                    self.df = self.cleaner.clean(self.df)

                elif choice == "3":
                    self._require_data()
                    self.df = self.feature_builder.build_features(self.df)

                elif choice == "4":
                    self._require_data()
                    self.df = self.risk_scorer.score(self.df)

                elif choice == "5":
                    self._require_data()
                    self.df = self.flagger.flag(self.df)

                elif choice == "6":
                    self._require_data()
                    self.reporter.generate(self.df)

                elif choice == "7":
                    self._require_data()

                    total_rows, total_cols = self.df.shape

                    print("\ndataset Summary  ")
                    print(f"total rows    : {total_rows:,}")

                    print("\nRisk Level Distribution")
                    risk_counts = self.df["risk_level"].value_counts()
                    risk_percent = (risk_counts / total_rows) * 100

                    summary_df = (
                        risk_counts
                        .to_frame(name="count")
                        .assign(percentage=risk_percent.round(2))
                    )

                    print(summary_df)


                elif choice == "0":
                    print("exiting application ")
                    break

                else:
                    print("invalid option")

            except Exception as e:
                print(f"error: {e}")

    def _require_data(self):
        if self.df is None:
            raise RuntimeError("load the dataset firstly")


if __name__ == "__main__":
    ConsoleApp().run()
