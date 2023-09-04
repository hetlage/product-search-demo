def test_ping(client):
    """
    GIVEN a Flask application
    WHEN the '/ping' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get("/ping")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "message" in json_data
