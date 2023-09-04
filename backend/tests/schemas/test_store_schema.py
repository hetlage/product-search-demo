import pytest

from app.schemas.store_schema import StoreSchema

def test_valid_store_schema():
    data = {
        "_id": "store1",
        "name": "Best Buy",
        "location": {"latitude": 40.7128, "longitude": -74.0060},
        "address": "123 Main St, New York, NY",
        "phone": "212-555-1234"
    }

    errors = StoreSchema().validate(data)

    assert errors == {}

def test_invalid_store_schema():
    data = {
        "_id": "store1",
        "name": 0,
        "address": 0
    }

    errors = StoreSchema().validate(data)

    assert "name" in errors
    assert "address" in errors