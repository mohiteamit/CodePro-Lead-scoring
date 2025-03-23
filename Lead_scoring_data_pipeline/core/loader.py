## -------------------------------------------
## File: Lead_scoring_data_pipeline/core/loader.py
## -------------------------------------------

import pandas as pd
import sqlite3
from Lead_scoring_data_pipeline.constants import LEADSCORING_CSV, DB_FILEPATH, RAW_TABLE_NAME

class DataLoader:
    def __init__(self, csv_path=LEADSCORING_CSV, db_path=DB_FILEPATH, table_name=RAW_TABLE_NAME):
        self.csv_path = csv_path
        self.db_path = db_path
        self.table_name = table_name

    def load_csv_to_db(self):
        df = pd.read_csv(self.csv_path)
        conn = sqlite3.connect(self.db_path)
        df.to_sql(self.table_name, conn, if_exists='replace', index=False)
        conn.close()
        return True