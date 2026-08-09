import pandas as pd

def load_data():
    constituents_df = pd.read_csv("data/constituents.csv")
    prices_df = pd.read_csv("data/prices.csv", parse_dates=["date"])
    portfolio_df = pd.read_csv("data/portfolio.csv", parse_dates=["date"])

    return constituents_df, prices_df, portfolio_df

if __name__ == "__main__":
    constituents_df, prices_df, portfolio_df = load_data()

    print("CONSTITUENTS")
    print(constituents_df)
    print("\nPRICES")
    print(prices_df)
    print("\nPORTFOLIO")
    print(portfolio_df)