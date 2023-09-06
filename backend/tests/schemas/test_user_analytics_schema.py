import pytest

from app.schemas.user_analytics_schema import UserAnalyticsSchema


def test_valid_user_analytics_schema():
    data = {
        "_id": "user_analytics1",
        "user_id": "user1",
        "search_term": "iPhone",
        "search_location": {"latitude": 40.7128, "longitude": -74.0060},
        "timestamp": "2023-08-24T12:34:56Z",
    }

    errors = UserAnalyticsSchema().validate(data)

    assert errors == {}


def test_invalid_user_analytics_schema():
    data = {
        "_id": "user_analytics1",
        "search_term": 0,
        "search_location": {"latitude": "invalid", "longitude": -74.0060},
    }

    errors = UserAnalyticsSchema().validate(data)

    assert "search_term" in errors
    assert "search_location" in errors
