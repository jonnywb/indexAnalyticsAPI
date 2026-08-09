import pandas as pd
from app.services.load_data import load_data
from app.services.validators import validate_prices

def calculate_market_caps_for_date(target_date):
    constituents_df, prices_df, _ = load_data()
    validate_prices(prices_df)

    daily_prices = prices_df[prices_df["date"] == target_date].copy()
    merged_df = daily_prices.merge(constituents_df, on="ticker", how="inner")

    merged_df["market_cap"] = merged_df["close_price"] * merged_df["shares_outstanding"]
    total_market_cap = merged_df["market_cap"].sum()
    merged_df["weight"] = merged_df["market_cap"] / total_market_cap

    return merged_df[["date", "ticker", "name", "close_price", "shares_outstanding", "market_cap", "weight"]]

def calculate_index_levels():
    constituents_df, prices_df, _ = load_data()

    merged_df = prices_df.merge(constituents_df, on="ticker", how="inner")
    merged_df["market_cap"] = merged_df["close_price"] * merged_df["shares_outstanding"]

    daily_index = (
        merged_df.groupby("date", as_index=False)["market_cap"]
        .sum()
        .sort_values("date")
    )

    base_market_cap = daily_index.iloc[0]["market_cap"]
    daily_index["index_level"] = (daily_index["market_cap"] / base_market_cap) * 100
    daily_index["daily_return"] = daily_index["index_level"].pct_change()

    return daily_index

def calculate_portfolio_performance():
    _, prices_df, portfolio_df = load_data()

    merged_df = prices_df.merge(portfolio_df, on=["ticker", "date"], how="inner")
    merged_df["position_value"] = merged_df["units_held"] * merged_df["close_price"]

    portfolio_performance = (
        merged_df.groupby("date", as_index=False)["position_value"].sum()
        .sort_values("date").reset_index(drop=True)
    )

    portfolio_performance["portfolio_return"] = portfolio_performance["position_value"].pct_change()

    return portfolio_performance

def calculate_active_return():
    portfolio_df = calculate_portfolio_performance()
    benchmark_df = calculate_index_levels()
    benchmark_columns = benchmark_df[["date", "index_level", "daily_return"]]

    merged_df = portfolio_df.merge(benchmark_columns, on="date", how="inner")
    merged_df["active_return"] = merged_df["portfolio_return"] - merged_df["daily_return"]

    return merged_df

if __name__ == "__main__":
    print("MARKET CAPS FOR 2026-01-02")
    target_date = pd.Timestamp("2026-01-02")
    result_df = calculate_market_caps_for_date(target_date)
    print(result_df)

    print("\nTotal weight:", result_df["weight"].sum())

    print("\nINDEX LEVELS")
    index_levels_df = calculate_index_levels()
    print(index_levels_df)
