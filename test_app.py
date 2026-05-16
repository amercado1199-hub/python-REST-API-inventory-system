from app import app

import pytest

@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200


def test_get_single_item(client):
    response = client.get("/inventory/1")

    assert response.status_code == 200


def test_add_item(client):
    response = client.post(
        "/inventory",
        json={
            "name": "Test Item",
            "brand": "Test Brand",
            "price": 9.99,
            "stock": 5
        }
    )

    assert response.status_code == 201


def test_update_item(client):
    response = client.patch(
        "/inventory/1",
        json={
            "price": 15.99
        }
    )

    assert response.status_code == 200


def test_delete_item(client):
    response = client.delete("/inventory/1")
    assert response.status_code == 200

