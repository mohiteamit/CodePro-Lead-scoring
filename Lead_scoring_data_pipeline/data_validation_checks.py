## -------------------------------------------
## File: Lead_scoring_data_pipeline/data_validation_checks.py
## -------------------------------------------

import sqlite3
from Lead_scoring_data_pipeline.constants import DB_FILEPATH, RAW_TABLE_NAME

def data_shape_check(expected_rows, expected_cols):
    conn = sqlite3.connect(DB_FILEPATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {RAW_TABLE_NAME}")
    data = cursor.fetchall()
    conn.close()
    return len(data) == expected_rows and len(data[0]) == expected_cols
