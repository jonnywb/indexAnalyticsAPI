from flask import jsonify
import pandas as pd

from app.services.index_calculator import calculate_index_levels, calculate_portfolio_performance, calculate_active_return, calculate_market_caps_for_date

def register_routes(app):
    @app.route("/health")
    def health():
        return jsonify({
            "status": "ok",
            "message": "Healthy"
        })

    @app.route("/index-levels")
    def index_levels():
        index_levels_df = calculate_index_levels()
        index_levels_df_converted = index_levels_df.copy(deep=True)

        # Convert date to date str
        index_levels_df_converted["date"] = index_levels_df_converted["date"].dt.strftime("%Y-%m-%d")

        index_levels_dict = index_levels_df_converted.to_dict(orient="records")

        for row in index_levels_dict:
            if pd.isna(row["daily_return"]):
                row["daily_return"] = None
        return jsonify({"data": index_levels_dict})

    @app.route("/portfolio-performance")
    def portfolio_performance():
        portfolio_performance_df = calculate_portfolio_performance()

        portfolio_performance_dict = portfolio_performance_df.to_dict(orient="records")
        return jsonify(portfolio_performance_dict)

    @app.route("/active-return")
    def active_return():
        active_return_df = calculate_active_return()

        active_return_dict = active_return_df.to_dict(orient="records")
        return jsonify(active_return_dict)

    