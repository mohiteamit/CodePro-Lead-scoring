## -------------------------------------------
## File: Lead_scoring_inference_pipeline/core/predictor.py
## -------------------------------------------

import sqlite3
import pandas as pd
from pycaret.classification import load_model, predict_model
from Lead_scoring_inference_pipeline.constants import DB_FILEPATH, INFERENCE_TABLE, MODEL_PATH, PREDICTION_OUTPUT_FILE

class ModelPredictor:
    def __init__(self, db_path=DB_FILEPATH):
        self.conn = sqlite3.connect(db_path)

    def predict(self):
        model = load_model(MODEL_PATH)
        df = pd.read_sql(f"SELECT * FROM {INFERENCE_TABLE}", self.conn)
        predictions = predict_model(model, data=df)

        # Save prediction distribution
        distribution = predictions['prediction_label'].value_counts(normalize=True)
        with open(PREDICTION_OUTPUT_FILE, 'w') as f:
            f.write(distribution.to_string())

        return predictions