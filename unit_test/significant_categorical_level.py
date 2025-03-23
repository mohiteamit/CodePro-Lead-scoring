from Lead_scoring_data_pipeline.mapping import significant_categorical_level

def test_mapping_lists():
    assert isinstance(significant_categorical_level.list_platform, list)
    assert isinstance(significant_categorical_level.list_medium, list)
    assert isinstance(significant_categorical_level.list_source, list)
