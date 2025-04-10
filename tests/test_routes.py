def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200


def test_about_route(client):
    response = client.get("/about")
    assert response.status_code == 200
