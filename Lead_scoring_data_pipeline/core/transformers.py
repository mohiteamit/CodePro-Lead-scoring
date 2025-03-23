## -------------------------------------------
## File: Lead_scoring_data_pipeline/core/transformers.py
## -------------------------------------------

import sqlite3
import pandas as pd
import importlib.util

from Lead_scoring_data_pipeline.constants import (
    DB_FILEPATH, RAW_TABLE_NAME, CLEANED_TABLE_NAME,
    CITY_TIER_MAPPING_FILE, SIGNIFICANT_CATEGORICAL_LEVEL_FILE, INTERACTION_MAPPING_FILE
)

class DataTransformer:
    def __init__(self, db_path=DB_FILEPATH):
        self.conn = sqlite3.connect(db_path)

    def _load_mapping_dict(self, file_path, variable_name):
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        return getattr(foo, variable_name)

    def map_city_tier(self):
        city_tier_mapping = self._load_mapping_dict(CITY_TIER_MAPPING_FILE, 'city_tier_mapping')
        df = pd.read_sql(f"SELECT * FROM {RAW_TABLE_NAME}", self.conn)
        df['city_tier'] = df['city_tier'].map(city_tier_mapping).fillna(3.0)
        df.to_sql(CLEANED_TABLE_NAME, self.conn, if_exists='replace', index=False)

    def map_categorical_vars(self):
        significant_map = self._load_mapping_dict(SIGNIFICANT_CATEGORICAL_LEVEL_FILE, 'list_platform',)
        df = pd.read_sql(f"SELECT * FROM {CLEANED_TABLE_NAME}", self.conn)
        df['first_platform_c'] = df['first_platform_c'].apply(lambda x: x if x in significant_map else 'others')
        df['first_utm_medium_c'] = df['first_utm_medium_c'].apply(lambda x: x if x in self._load_mapping_dict(SIGNIFICANT_CATEGORICAL_LEVEL_FILE, 'list_medium') else 'others')
        df['first_utm_source_c'] = df['first_utm_source_c'].apply(lambda x: x if x in self._load_mapping_dict(SIGNIFICANT_CATEGORICAL_LEVEL_FILE, 'list_source') else 'others')
        df.to_sql(CLEANED_TABLE_NAME, self.conn, if_exists='replace', index=False)

    def interactions_mapping(self):
        df = pd.read_sql(f"SELECT * FROM {CLEANED_TABLE_NAME}", self.conn)
        mapping_df = pd.read_csv(INTERACTION_MAPPING_FILE)
        interaction_cols = list(mapping_df.columns)
        df = df[interaction_cols + [col for col in df.columns if col not in interaction_cols]]
        for interaction_type in mapping_df.columns:
            df[interaction_type] = df[mapping_df[interaction_type].dropna().tolist()].sum(axis=1)
        df.drop(columns=interaction_cols, inplace=True)
        df.to_sql(CLEANED_TABLE_NAME, self.conn, if_exists='replace', index=False)