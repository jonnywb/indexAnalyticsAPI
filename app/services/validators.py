def validate_prices(prices_df):
    required_columns = ["date", "ticker", "close_price"]
    if prices_df[required_columns].isna().any().any():
        raise ValueError("Prices data contains missing required values")

    duplicate_columns = ["date", "ticker"]
    if prices_df.duplicated(subset=duplicate_columns).any():
        raise ValueError("Prices data contains duplicate values")