## -------------------------------------------
## File: Lead_scoring_training_pipeline/core/trainer.py
## -------------------------------------------

import pandas as pd
import sqlite3
import mlflow
from pycaret.classification import setup, compare_models, pull, save_model

from Lead_scoring_training_pipeline.constants import DB_FILEPATH, MODEL_INPUT_TABLE, TARGET_COL, MLFLOW_DB_PATH

class ModelTrainer:
    def __init__(self, db_path=DB_FILEPATH):
        self.db_path = db_path

    def train(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql(f"SELECT * FROM {MODEL_INPUT_TABLE}", conn)
        conn.close()

        # PyCaret setup
        s = setup(data=df, target=TARGET_COL, session_id=123, silent=True, html=False)
        best_model = compare_models()
        model_results = pull()

        # Save model
        save_model(best_model, "LeadScoringModel")

        # MLflow logging
        mlflow.set_tracking_uri(f"sqlite:///{MLFLOW_DB_PATH}")
        mlflow.set_experiment("Lead Scoring Experiment")
        with mlflow.start_run():
            mlflow.log_params({"target": TARGET_COL})
            mlflow.log_artifact("LeadScoringModel.pkl")

        return best_model