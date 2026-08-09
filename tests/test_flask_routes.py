from app import create_app

def test_index_levels_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/index-levels")
    json_data = response.get_json()

    assert response.status_code == 200
    assert "data" in json_data
    assert isinstance(json_data["data"], list)
    assert "date" in json_data["data"][0]
    assert "index_level" in json_data["data"][0]

def test_active_return_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/active-return")
    json_data = response.get_json()

    assert response.status_code == 200
    assert "data" in json_data
    assert isinstance(json_data["data"], list)
    assert "portfolio_return" in json_data["data"][0]
    assert "daily_return" in json_data["data"][0]
    assert "active_return" in json_data["data"][0]