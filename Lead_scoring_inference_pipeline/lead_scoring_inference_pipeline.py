## -------------------------------------------
## File: Lead_scoring_inference_pipeline/lead_scoring_inference_pipeline.py
## -------------------------------------------

from Lead_scoring_inference_pipeline.utils import get_models_prediction, input_features_check, prediction_ratio_check

if __name__ == "__main__":
    if input_features_check():
        preds = get_models_prediction()
        assert prediction_ratio_check(preds)
    else:
        raise ValueError("Input feature validation failed")