## -------------------------------------------
## File: Lead_scoring_data_pipeline/constants.py
## -------------------------------------------

# Config for data paths and database locations

# Input CSV files (update filenames if needed)
DATA_DIRECTORY = "Lead_scoring_data_pipeline/data/"
LEADSCORING_CSV = DATA_DIRECTORY + "leadscoring.csv"
LEADSCORING_INFERENCE_CSV = DATA_DIRECTORY + "leadscoring_inference_final_v2.csv"

# SQLite DB path (central DB used in all stages)
DB_FILEPATH = "Lead_scoring_data_pipeline/lead_scoring_data_cleaning.db"

# Mapping files
MAPPING_DIRECTORY = "Lead_scoring_data_pipeline/mapping/"
CITY_TIER_MAPPING_FILE = MAPPING_DIRECTORY + "city_tier_mapping.py"
SIGNIFICANT_CATEGORICAL_LEVEL_FILE = MAPPING_DIRECTORY + "significant_categorical_level.py"
INTERACTION_MAPPING_FILE = MAPPING_DIRECTORY + "interaction_mapping.csv"

# Table name for raw and cleaned data
RAW_TABLE_NAME = "loaded_data"
CLEANED_TABLE_NAME = "model_input"