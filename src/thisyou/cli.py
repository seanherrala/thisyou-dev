"""Command-line entry point for thisyou."""

from __future__ import annotations

from .project_overview import create_project_overview


def main() -> None:
    print("thisyou.dev")
    print("Let the picture speak.")
    print()
    print("Project signals:")

    for signal in create_project_overview():
        focus = ", ".join(signal.focus)
        print(f"- {signal.name}: {signal.description} Focus: {focus}.")


if __name__ == "__main__":
    main()
