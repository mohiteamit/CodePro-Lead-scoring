## -------------------------------------------
## File: Lead_scoring_data_pipeline/utils.py
## (WRAPPER for evaluator - must match function name)
## -------------------------------------------

from Lead_scoring_data_pipeline.core.database import DatabaseBuilder
from Lead_scoring_data_pipeline.core.loader import DataLoader
from Lead_scoring_data_pipeline.core.transformers import DataTransformer

# EVALUATOR FUNCTION WRAPPERS

def build_dbs():
    builder = DatabaseBuilder()
    builder.build()

def load_data_into_db():
    loader = DataLoader()
    loader.load_csv_to_db()

def map_city_tier():
    transformer = DataTransformer()
    transformer.map_city_tier()

def map_categorical_vars():
    transformer = DataTransformer()
    transformer.map_categorical_vars()

def interactions_mapping():
    transformer = DataTransformer()
    transformer.interactions_mapping()