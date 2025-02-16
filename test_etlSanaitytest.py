import pytest
import pandas as pd

def test_checkDuplicates():
    target_df = pd.read_csv("target.csv",sep=",")
    count = target_df.duplicated().sum()
    assert count == 0
