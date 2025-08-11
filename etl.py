import pandas as pd
import os
from sqlalchemy import create_engine

class FriendlyETL:
    def __init__(self, source_path, destination_path, transform_condition):
        self.source_path = source_path
        self.destination_path = destination_path
        self.transform_condition = transform_condition
        self.df = None

    def extract(self):
        if self.source_path.endswith('.csv'):
            self.df = pd.read_csv(self.source_path)
            print("✅ Extracted CSV file.")
        elif self.source_path.endswith('.json'):
            self.df = pd.read_json(self.source_path)
            print("✅ Extracted JSON file.")
        elif self.source_path.endswith('.xlsx'):
            self.df = pd.read_excel(self.source_path)
            print("✅ Extracted Excel file.")
        elif self.source_path.startswith("mysql://") or self.source_path.startswith("sqlite:///"):
            engine = create_engine(self.source_path)
            self.df = pd.read_sql("SELECT * FROM source_table", engine)  # Update table name if needed
            print("✅ Extracted from database.")
        else:
            raise ValueError("❌ Unsupported source format. Use CSV, JSON, Excel, or database path.")

    def transform(self):
        if not self.transform_condition:
            raise ValueError("❌ Transform condition is required.")

        print(f"🔧 Applying transformations: {self.transform_condition}")
        conditions = self.transform_condition.split(',')

        for cond in conditions:
            cond = cond.strip().lower()
            if cond == "remove_duplicates":
                self.df.drop_duplicates(inplace=True)
                print("✅ Removed duplicates.")
            elif cond == "remove_nulls":
                self.df.dropna(inplace=True)
                print("✅ Removed null values.")
            elif cond == "handle_missing_data":
                self.df.ffill(inplace=True)                # forward fill
                print("✅ Handled missing data with forward fill.")
            elif cond == "validate_data":
                self.df = self.df.dropna(subset=self.df.columns[:1])  # Example: ensure 1st column has no NaNs
                print("✅ Basic data validation applied.")
            else:
                print(f"⚠️ Unknown transformation: {cond}")

    def load(self):
        if self.destination_path.endswith('.csv'):
            self.df.to_csv(self.destination_path, index=False)
            print("✅ Data saved as CSV.")
        elif self.destination_path.endswith('.json'):
            self.df.to_json(self.destination_path, orient='records', lines=True)
            print("✅ Data saved as JSON.")
        elif self.destination_path.endswith('.xlsx'):
            self.df.to_excel(self.destination_path, index=False)
            print("✅ Data saved as Excel.")
        elif self.destination_path.startswith("mysql://") or self.destination_path.startswith("sqlite:///"):
            engine = create_engine(self.destination_path)
            self.df.to_sql("destination_table", con=engine, if_exists='replace', index=False)
            print("✅ Data loaded into database.")
        else:
            raise ValueError("❌ Unsupported destination format. Use .csv, .json, .xlsx, or a database path.")

    def run(self):
        print("🚀 Starting Friendly ETL process...")
        self.extract()
        self.transform()
        self.load()
        print("🏁 ETL process completed successfully.")


def run_etl(source_path, destination_path, transform_condition):
    etl = FriendlyETL(source_path, destination_path, transform_condition)
    etl.run()

