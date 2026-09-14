"""Profile lookup boundary for the web application."""

import re
from collections import Counter
from dataclasses import dataclass
from typing import Any

import httpx

HANDLE_PATTERN = re.compile(r"^[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")
BLUESKY_API_BASE_URL = "https://public.api.bsky.app/xrpc"


@dataclass(frozen=True)
class Profile:
    handle: str
    display_name: str
    description: str
    followers: int
    following: int
    top_interactions: tuple[str, ...]


class ProfileLookupError(RuntimeError):
    """Raised when Bluesky cannot provide a profile."""


def normalize_handle(handle: str) -> str | None:
    """Normalize a Bluesky handle and reject values outside handle syntax."""
    clean_handle = handle.strip().lstrip("@").lower()
    if not clean_handle or len(clean_handle) > 253 or not HANDLE_PATTERN.fullmatch(clean_handle):
        return None
    return clean_handle


def get_profile(handle: str, client: httpx.Client | None = None) -> Profile:
    """Fetch a public profile and recent interaction data from Bluesky."""
    clean_handle = normalize_handle(handle)
    if clean_handle is None:
        raise ValueError("Invalid Bluesky handle")

    owns_client = client is None
    api_client = client or httpx.Client(base_url=BLUESKY_API_BASE_URL, timeout=10.0)
    try:
        profile_response = api_client.get(
            "/app.bsky.actor.getProfile",
            params={"actor": clean_handle},
        )
        profile_response.raise_for_status()
        profile_data = profile_response.json()

        feed_response = api_client.get(
            "/app.bsky.feed.getAuthorFeed",
            params={"actor": clean_handle, "limit": 50},
        )
        feed_response.raise_for_status()
        feed_data = feed_response.json()
    except httpx.HTTPStatusError as error:
        if error.response.status_code == 400:
            raise ProfileLookupError("That handle was not found on Bluesky.") from error
        raise ProfileLookupError("Bluesky did not return the profile right now.") from error
    except httpx.RequestError as error:
        raise ProfileLookupError("Bluesky is unavailable right now. Try again shortly.") from error
    finally:
        if owns_client:
            api_client.close()

    return Profile(
        handle=str(profile_data["handle"]),
        display_name=str(profile_data.get("displayName") or profile_data["handle"]),
        description=str(profile_data.get("description") or "No profile description yet."),
        followers=int(profile_data.get("followersCount") or 0),
        following=int(profile_data.get("followsCount") or 0),
        top_interactions=_top_interactions(feed_data),
    )


def _top_interactions(feed_data: dict[str, Any]) -> tuple[str, ...]:
    authors = (
        item["post"]["author"]["handle"]
        for item in feed_data.get("feed", [])
        if item.get("post", {}).get("author", {}).get("handle")
    )
    return tuple(handle for handle, _ in Counter(authors).most_common(5))
