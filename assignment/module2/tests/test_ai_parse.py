import arrow
import pytest
from arrow.parser import ParserError


def test_parse_iso_date():
    assert arrow.get("2026-09-08").format("YYYY-MM-DD") == "2026-09-08"


def test_parse_timestamp_zero():
    assert arrow.get(0).format("YYYY-MM-DD HH:mm:ss") == "1970-01-01 00:00:00"


def test_parse_negative_timestamp():
    assert arrow.get(-1).format("YYYY-MM-DD HH:mm:ss") == "1969-12-31 23:59:59"


def test_parse_datetime_with_timezone_keeps_offset():
    value = arrow.get("2026-09-08T10:00:00+08:00")
    assert value.format("YYYY-MM-DD HH:mm:ss ZZ") == "2026-09-08 10:00:00 +08:00"


def test_parse_invalid_month_raises_value_error():
    with pytest.raises(ValueError):
        arrow.get("2026-13-01")


def test_parse_invalid_day_raises_value_error():
    with pytest.raises(ValueError):
        arrow.get("2026-02-30")


def test_parse_empty_string_raises_parser_error():
    with pytest.raises(ParserError):
        arrow.get("")


def test_parse_none_raises_type_error():
    with pytest.raises(TypeError):
        arrow.get(None)
