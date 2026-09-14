from fastapi.testclient import TestClient
from pytest import MonkeyPatch

from thisyou.app import app
from thisyou.profile_service import Profile

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home_page_contains_handle_form() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert 'name="handle"' in response.text


def test_profile_page_renders_profile_card(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "thisyou.app.get_profile",
        lambda handle: Profile(
            handle=handle,
            display_name="Example",
            description="A test profile.",
            followers=12,
            following=34,
            top_interactions=("friend.bsky.social",),
        ),
    )

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
