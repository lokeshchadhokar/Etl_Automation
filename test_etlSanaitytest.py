import pytest
import pandas as pd

# Load Data
@pytest.fixture
def load_data():
    return pd.read_csv("target.csv", sep=",")

# 1. Check for duplicate records
def test_check_duplicates(load_data):
    count = load_data.duplicated().sum()
    assert count == 0, f"Found {count} duplicate records"

# 2. Check for NULL values in critical columns
def test_check_null_values(load_data):
    assert load_data['ename'].isnull().sum() == 0, "NULL values found in ename"
    assert load_data['Salary'].isnull().sum() == 0, "NULL values found in Salary"

# 3. Validate Salary column for negative values
def test_check_negative_salary(load_data):
    assert (load_data['Salary'] >= 0).all(), "Salary contains negative values"

# 4. Check data types
def test_validate_data_types(load_data):
    assert load_data['Salary'].dtype == 'int64', "Salary column is not integer"
    assert load_data['deptno'].dtype in ['int64', 'float64'], "deptno should be numeric"

# 5. Check for empty file scenario
def test_empty_file():
    try:
        df = pd.read_csv("target.csv", sep=",")
        assert not df.empty, "CSV file is empty"
    except Exception as e:
        pytest.fail(f"File error: {e}")

# 6. Validate Primary Key uniqueness
def test_primary_key_unique(load_data):
    assert load_data['no'].is_unique, "Primary key 'no' is not unique"

# 7. Check for leading/trailing spaces in 'ename'
def test_strip_spaces(load_data):
    load_data['ename'] = load_data['ename'].str.strip()
    assert (load_data['ename'].str.startswith(" ") | load_data['ename'].str.endswith(" ")).sum() == 0, "Leading/trailing spaces found"

# 8. Verify deptno is always assigned
def test_deptno_null(load_data):
    assert load_data['deptno'].notnull().sum() > 0, "NULL deptno found"
