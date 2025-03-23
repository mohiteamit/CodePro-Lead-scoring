## -------------------------------------------
## File: Lead_scoring_training_pipeline/lead_scoring_training_pipeline.py
## -------------------------------------------

from Lead_scoring_training_pipeline.utils import get_trained_model, encode_features

if __name__ == "__main__":
    encode_features()
    get_trained_model()