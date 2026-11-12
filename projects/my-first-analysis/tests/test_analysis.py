import pandas as pd
import pytest

from src.analysis import validate_required_columns


def test_validate_required_columns_passes():
    validate_required_columns(pd.DataFrame({"date": [], "price": []}), ["date", "price"])


def test_validate_required_columns_reports_missing():
    with pytest.raises(ValueError, match="price"):
        validate_required_columns(pd.DataFrame({"date": []}), ["date", "price"])
