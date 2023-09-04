import pytest

from app.schemas.product_schema import ProductSchema


def test_valid_product_schema():
    data = {
        "_id": "product1",
        "name": "Apple iPhone 12",
        "category": "Electronics",
        "description": "Latest model of the Apple iPhone",
        "price": 999.99,
        "image_url": "http://example.com/image.jpg",
    }

    errors = ProductSchema().validate(data)

    assert errors == {}


def test_invalid_product_schema():
    data = {
        "_id": "product1",
        "name": 0,
        "price": "invalid",
    }

    errors = ProductSchema().validate(data)

    assert "name" in errors
    assert "price" in errors
