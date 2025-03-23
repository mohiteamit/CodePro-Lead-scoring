## -------------------------------------------
## File: unit_test/utils.py
## -------------------------------------------

import unittest
from Lead_scoring_data_pipeline import utils
from Lead_scoring_data_pipeline import data_validation_checks
from Lead_scoring_data_pipeline import schema

class TestDataPipeline(unittest.TestCase):

    def test_build_and_load_db(self):
        utils.build_dbs()
        utils.load_data_into_db()
        self.assertTrue(
            data_validation_checks.data_shape_check(
                schema.SCHEMA["expected_rows"],
                schema.SCHEMA["expected_columns"]
            )
        )

    def test_city_tier_mapping(self):
        utils.map_city_tier()
        # Additional checks can be added here

    def test_categorical_mapping(self):
        utils.map_categorical_vars()
        # Additional checks can be added here

    def test_interaction_mapping(self):
        utils.interactions_mapping()
        # Additional checks can be added here

if __name__ == "__main__":
    unittest.main()
