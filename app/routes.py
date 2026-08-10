from flask import jsonify, render_template
import pandas as pd

from app.services.index_calculator import calculate_index_levels, calculate_portfolio_performance, calculate_active_return, calculate_market_caps_for_date

def register_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

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
        portfolio_perf_converted = portfolio_performance_df.copy(deep=True)

        portfolio_perf_converted["date"] = portfolio_perf_converted["date"].dt.strftime("%Y-%m-%d")

        portfolio_performance_dict = portfolio_perf_converted.to_dict(orient="records")

        for row in portfolio_performance_dict:
            if pd.isna(row["portfolio_return"]):
                row["portfolio_return"] = None
        return jsonify({"data": portfolio_performance_dict})

    @app.route("/active-return")
    def active_return():
        active_return_df = calculate_active_return()
        converted_active_return = active_return_df.copy(deep=True)

        converted_active_return["date"] = converted_active_return["date"].dt.strftime("%Y-%m-%d")

        active_return_dict = converted_active_return.to_dict(orient="records")

        #active_return, daily_return, portfolio_return
        for row in active_return_dict:
            if pd.isna(row["active_return"]):
                row["active_return"] = None
            if pd.isna(row["daily_return"]):
                row["daily_return"] = None
            if pd.isna(row["portfolio_return"]):
                row["portfolio_return"] = None

        return jsonify({"data": active_return_dict})

    