from Lead_scoring_data_pipeline import utils

if __name__ == "__main__":
    utils.build_dbs()
    utils.load_data_into_db()
    utils.map_city_tier()
    utils.map_categorical_vars()
    utils.interactions_mapping()
