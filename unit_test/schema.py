from Lead_scoring_data_pipeline import schema

def test_schema_structure():
    assert "expected_columns" in schema.SCHEMA
    assert "expected_rows" in schema.SCHEMA
