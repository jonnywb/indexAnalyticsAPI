import pandas as pd
from app.services.load_data import load_data


def calculate_market_caps_for_date(target_date):
    constituents_df, prices_df, _ = load_data()

    daily_prices = prices_df[prices_df["date"] == target_date].copy()

    merged_df = daily_prices.merge(constituents_df, on="ticker", how="inner")

    merged_df["market_cap"] = merged_df["close_price"] * merged_df["shares_outstanding"]

    total_market_cap = merged_df["market_cap"].sum()

    merged_df["weight"] = merged_df["market_cap"] / total_market_cap

    return merged_df[["date", "ticker", "name", "close_price", "shares_outstanding", "market_cap", "weight"]]


if __name__ == "__main__":
    target_date = pd.Timestamp("2026-01-02")
    result_df = calculate_market_caps_for_date(target_date)

    print(result_df)
    print("\nTotal weight:", result_df["weight"].sum())
