import pytest
from ungoliant.tools import polygon_tools as pg

def test_get_open_close_price():
    result = pg.get_open_close_price("AAPL", "2025-02-07")
    assert result["status"] == "OK"
    print(result)

def test_get_open_close_price():
    result = pg.get_open_close_price("AAPL", "2025-02-07")
    assert result["status"] == "OK"
    print(result)

if __name__ == "__main__":
    test_get_open_close_price()