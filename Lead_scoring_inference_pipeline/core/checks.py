## -------------------------------------------
## File: Lead_scoring_inference_pipeline/core/checks.py
## -------------------------------------------

import pandas as pd
import sqlite3
from Lead_scoring_inference_pipeline.constants import DB_FILEPATH, INFERENCE_TABLE

class PredictionChecks:
    def __init__(self, db_path=DB_FILEPATH):
        self.conn = sqlite3.connect(db_path)

    def input_features_check(self):
        df = pd.read_sql(f"SELECT * FROM {INFERENCE_TABLE}", self.conn)
        return df.isnull().sum().sum() == 0  # Ensure no missing values

    def prediction_ratio_check(self, predictions):
        counts = predictions['prediction_label'].value_counts(normalize=True)
        return all(0.0 <= ratio <= 1.0 for ratio in counts)