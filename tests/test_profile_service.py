import httpx

from thisyou.profile_service import get_profile, normalize_handle


def test_normalize_handle() -> None:
    assert normalize_handle(" @Example.Bsky.Social ") == "example.bsky.social"
    assert normalize_handle("not a handle") is None


def test_get_profile_reads_bluesky_responses() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("getProfile"):
            return httpx.Response(
                200,
                json={
                    "handle": "example.bsky.social",
                    "displayName": "Example",
                    "description": "A real profile.",
                    "followersCount": 42,
                    "followsCount": 17,
                },
            )
        return httpx.Response(
            200,
            json={
                "feed": [
                    {"post": {"author": {"handle": "friend.bsky.social"}}},
                    {"post": {"author": {"handle": "friend.bsky.social"}}},
                    {"post": {"author": {"handle": "other.bsky.social"}}},
                ]
            },
        )

    with httpx.Client(
        transport=httpx.MockTransport(handler),
        base_url="https://public.api.bsky.app/xrpc",
    ) as client:
        profile = get_profile("@example.bsky.social", client)

    assert profile.display_name == "Example"
    assert profile.followers == 42
    assert profile.following == 17
    assert profile.top_interactions == (
        "friend.bsky.social",
        "other.bsky.social",
    )
