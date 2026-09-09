import arrow


BASE = arrow.get("2026-01-09T00:00:00+00:00")


def test_humanize_three_days_past():
    assert BASE.shift(days=-3).humanize(BASE) == "3 days ago"


def test_humanize_three_days_future():
    assert BASE.shift(days=3).humanize(BASE) == "in 3 days"


def test_humanize_16_days_same_month_should_be_two_weeks():
    # 疑似缺陷：Arrow 1.4.0 实际输出为 "in a month"，
    # 与 GitHub issue #1240 描述的用户预期 "in 2 weeks" 不一致。
    assert BASE.shift(days=16).humanize(BASE) == "in 2 weeks"
