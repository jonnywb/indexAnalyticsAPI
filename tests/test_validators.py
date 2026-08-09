import pandas as pd
import pytest

from app.services.load_data import load_data
from app.services.validators import validate_prices

def test_validate_prices_raises_for_duplicate_date_ticker():
    _, prices_df, _ = load_data()

    duplicate_row = prices_df.iloc[[0]]
    prices_with_duplicate = pd.concat([prices_df, duplicate_row], ignore_index=True)

    with pytest.raises(ValueError, match="duplicate"):
        validate_prices(prices_with_duplicate)

def test_validate_prices_raises_for_missing_required_values():
    _, prices_df, _ = load_data()

    prices_df_missing_val = prices_df.copy(deep=True)
    prices_df_missing_val.at[2, 'close_price'] = None

    with pytest.raises(ValueError, match="missing"):
        validate_prices(prices_df_missing_val)