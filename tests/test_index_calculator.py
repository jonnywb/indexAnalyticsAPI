import pandas as pd
import pytest
from app.services.index_calculator import calculate_market_caps_for_date, calculate_index_levels, calculate_portfolio_performance, calculate_active_return


def test_market_caps_weights_sum_to_one():
    date = pd.Timestamp("2026-01-02")
    market_caps_for_date = calculate_market_caps_for_date(date)

    sum_of_weight = market_caps_for_date["weight"].sum()

    assert sum_of_weight == pytest.approx(1.0)

def test_market_caps_calculated_for_correct_date():
    target_date = pd.Timestamp("2026-01-02")

    calculated_market_caps = calculate_market_caps_for_date(target_date)
    assert (calculated_market_caps["date"] == target_date).all()

def test_calculate_index_levels_initial_return():
    calculated_index_levels = calculate_index_levels()

    assert pd.isna(calculated_index_levels.iloc[0]["daily_return"])

def test_calculate_portfolio_performance_initial_return():
    calculated_portfolio_performance = calculate_portfolio_performance()

    assert pd.isna(calculated_portfolio_performance.iloc[0]["portfolio_return"])

def test_calculate_active_return_initial_return():
    calculated_active_return = calculate_active_return()

    assert pd.isna(calculated_active_return.iloc[0]["active_return"])