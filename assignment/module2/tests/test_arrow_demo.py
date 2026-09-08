import arrow


def test_parse_iso_date():
    """解析 '2026-09-08' 这种标准日期字符串。"""
    assert arrow.get("2026-09-08").format("YYYY-MM-DD") == "2026-09-08"


def test_shift_one_day_crosses_february():
    """2026 年不是闰年，2 月 28 日加 1 天应为 3 月 1 日。"""
    assert arrow.get("2026-02-28").shift(days=1).format("YYYY-MM-DD") == "2026-03-01"


def test_timestamp_zero():
    """Unix 时间戳 0 对应 1970-01-01 00:00:00 UTC。"""
    assert arrow.get(0).format("YYYY-MM-DD HH:mm:ss") == "1970-01-01 00:00:00"


def test_invalid_month_raises_value_error():
    """月份只有 1 到 12，月份为 13 应抛出 ValueError。"""
    try:
        arrow.get("2026-13-01")
    except ValueError:
        return
    raise AssertionError("月份为 13 时应抛出 ValueError")
