## -------------------------------------------
## File: Lead_scoring_data_pipeline/core/database.py
## -------------------------------------------

import sqlite3
import os
from Lead_scoring_data_pipeline.constants import DB_FILEPATH

class DatabaseBuilder:
    def __init__(self, db_path=DB_FILEPATH):
        self.db_path = db_path

    def build(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        conn = sqlite3.connect(self.db_path)
        conn.close()
        return True