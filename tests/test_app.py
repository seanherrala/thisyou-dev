from fastapi.testclient import TestClient

from thisyou.app import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home_page_contains_handle_form() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert 'name="handle"' in response.text


def test_profile_page_renders_fixture_card() -> None:
    response = client.post("/profile", data={"handle": "@example.bsky.social"})

    assert response.status_code == 200
    assert "Example" in response.text
    assert "@example.bsky.social" in response.text


def test_profile_page_rejects_blank_handle() -> None:
    response = client.post("/profile", data={"handle": " "})

    assert response.status_code == 200
    assert "Give us a valid Bluesky handle first." in response.text


def test_profile_page_rejects_invalid_handle() -> None:
    response = client.post("/profile", data={"handle": "not a handle"})

    assert response.status_code == 200
    assert "Give us a valid Bluesky handle first." in response.text
