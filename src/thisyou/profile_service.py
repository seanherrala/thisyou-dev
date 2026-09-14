"""Profile lookup boundary for the web application."""

import re
from dataclasses import dataclass

HANDLE_PATTERN = re.compile(r"^[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")


@dataclass(frozen=True)
class Profile:
    handle: str
    display_name: str
    description: str
    followers: int
    following: int
    top_interactions: tuple[str, ...]


def normalize_handle(handle: str) -> str | None:
    """Normalize a Bluesky handle and reject values outside handle syntax."""
    clean_handle = handle.strip().lstrip("@").lower()
    if not clean_handle or len(clean_handle) > 253 or not HANDLE_PATTERN.fullmatch(clean_handle):
        return None
    return clean_handle


def get_profile(handle: str) -> Profile:
    """Return fixture data until the Bluesky client is connected."""
    clean_handle = normalize_handle(handle)
    if clean_handle is None:
        raise ValueError("Invalid Bluesky handle")

    return Profile(
        handle=clean_handle,
        display_name=clean_handle.split(".")[0].replace("-", " ").title(),
        description="A small picture of this orbit, for now.",
        followers=128,
        following=214,
        top_interactions=("someone.bsky.social", "another.bsky.social"),
    )
