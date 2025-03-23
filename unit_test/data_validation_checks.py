from Lead_scoring_data_pipeline import data_validation_checks

def test_data_shape_check():
    assert data_validation_checks.data_shape_check(1000, 22)
