import arrow


def test_format_basic_date():
    assert arrow.get("2026-09-08").format("YYYY-MM-DD") == "2026-09-08"


def test_format_full_weekday_and_month():
    assert arrow.get("2026-09-08").format("dddd, DD MMMM YYYY") == "Tuesday, 08 September 2026"


def test_format_datetime_with_time():
    assert arrow.get("2026-09-08T09:30:15").format("YYYY-MM-DD HH:mm:ss") == "2026-09-08 09:30:15"


def test_format_month_day():
    assert arrow.get("2026-12-25").format("MM/DD") == "12/25"
