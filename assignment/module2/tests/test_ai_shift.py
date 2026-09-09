import arrow
import pytest


def test_shift_non_leap_february_end():
    assert arrow.get("2026-02-28").shift(days=1).format("YYYY-MM-DD") == "2026-03-01"


def test_shift_leap_february_day():
    assert arrow.get("2024-02-28").shift(days=1).format("YYYY-MM-DD") == "2024-02-29"


def test_shift_back_one_day_crosses_year():
    assert arrow.get("2026-01-01").shift(days=-1).format("YYYY-MM-DD") == "2025-12-31"


def test_shift_add_month_clamps_to_month_end():
    assert arrow.get("2026-01-31").shift(months=1).format("YYYY-MM-DD") == "2026-02-28"


def test_shift_twelve_months_rolls_year():
    assert arrow.get("2026-03-15").shift(months=12).format("YYYY-MM-DD") == "2027-03-15"


def test_shift_invalid_unit_raises_value_error():
    with pytest.raises(ValueError):
        arrow.get("2026-01-01").shift(decades=1)
