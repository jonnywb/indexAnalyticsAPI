import pandas as pd
import pytest
from app.services.index_calculator import calculate_market_caps_for_date


def test_market_caps_weights_sum_to_one():
    date = pd.Timestamp("2026-01-02")
    market_caps_for_date = calculate_market_caps_for_date(date)

    sum_of_weight = market_caps_for_date["weight"].sum()

    assert sum_of_weight == pytest.approx(1.0)

def test_market_caps_calculated_for_correct_date():
    target_date = pd.Timestamp("2026-01-02")

    calculated_market_caps = calculate_market_caps_for_date(target_date)
    assert (calculated_market_caps["date"] == target_date).all()