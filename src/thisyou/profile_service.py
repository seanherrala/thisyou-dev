"""Profile lookup boundary for the web application."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Profile:
    handle: str
    display_name: str
    description: str
    followers: int
    following: int
    top_interactions: tuple[str, ...]


def get_profile(handle: str) -> Profile:
    """Return fixture data until the Bluesky client is connected."""
    clean_handle = handle.removeprefix("@")
    return Profile(
        handle=clean_handle,
        display_name=clean_handle.split(".")[0].replace("-", " ").title(),
        description="A small picture of this orbit, for now.",
        followers=128,
        following=214,
        top_interactions=("someone.bsky.social", "another.bsky.social"),
    )
