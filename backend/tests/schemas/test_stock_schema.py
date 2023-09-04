import pytest

from app.schemas.stock_schema import StockSchema


def test_valid_stock_schema():
    data = {
        "_id": "stock1",
        "product_id": "product1",
        "stores": [
            {
                "store_id": "A",
                "stock_level": 10,
                "last_restocked": "2023-08-01T10:00:00Z",
            },
            {
                "store_id": "B",
                "stock_level": 5,
                "last_restocked": "2023-08-02T11:00:00Z",
            },
        ],
    }

    errors = StockSchema().validate(data)

    assert errors == {}


def test_invalid_stock_schema():
    data = {
        "_id": 0,
        "product_id": 0,
        "stores": [{"store_id": "A", "stock_level": "invalid"}],
    }

    errors = StockSchema().validate(data)

    assert "_id" in errors
    assert "product_id" in errors
