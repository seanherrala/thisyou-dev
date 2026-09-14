"""Project overview helpers for thisyou."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ProjectSignal:
    name: str
    description: str
    focus: list[str] = field(default_factory=list)
    status: str = "scaffolded"


def create_project_overview() -> list[ProjectSignal]:
    return [
        ProjectSignal(
            name="Identity",
            description=(
                "thisyou.dev is a Bluesky-native visualization tool for observing account patterns."
            ),
            focus=["brand", "narrative", "signal clarity"],
            status="scaffolded",
        ),
        ProjectSignal(
            name="Graph",
            description="Track users, posts, replies, reposts, and clusters as a graph structure.",
            focus=["users", "edges", "clusters"],
            status="scaffolded",
        ),
        ProjectSignal(
            name="Analysis",
            description=(
                "Surface orbits, nests, loops, ratholes, and mutual-boost patterns in context."
            ),
            focus=["pattern detection", "context", "visual summaries"],
            status="in-progress",
        ),
    ]
