## -------------------------------------------
## File: Lead_scoring_inference_pipeline/utils.py
## -------------------------------------------

from Lead_scoring_inference_pipeline.core.predictor import ModelPredictor
from Lead_scoring_inference_pipeline.core.checks import PredictionChecks


def get_models_prediction():
    predictor = ModelPredictor()
    return predictor.predict()


def input_features_check():
    check = PredictionChecks()
    return check.input_features_check()


def prediction_ratio_check(predictions):
    check = PredictionChecks()
    return check.prediction_ratio_check(predictions)