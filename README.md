# thisyou.dev

A Bluesky-native visualization tool that reveals user patterns, clusters, repost loops, nests, ratholes, and interaction orbits.

## Purpose

thisyou helps surface the story embedded in a Bluesky account's behavior without moralizing. It lets the picture speak.

## Stack

This project is intentionally a Python-first codebase.

- Python 3.11+
- Pydantic for data validation (if we need typed payloads)
- pytest for tests
- a modular package layout under `src/thisyou`

## Project layout

- `src/thisyou/` — package code
- `tests/` — project tests
- `notes/` — product and tone guidance
- `project-brief.md` — canonical project brief

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -m uvicorn thisyou.app:app --reload
```

Open `http://127.0.0.1:8000` in your browser. The health endpoint is available at
`http://127.0.0.1:8000/health`.

Run the quality checks with:

```bash
ruff check .
mypy
pytest
```

## Deployment

The `render.yaml` file configures a free Render web service. Merging to `main` deploys the
application through the connected Render service.

## Bluesky access

The profile form uses Bluesky's public read-only API, so no account credentials are required.
It requests a public profile and the user's recent author feed to populate the initial card and
top interactions.

## Current status

The first Bluesky-backed profile slice is in place. The next steps are to define the user/post
graph model and add the first analysis pass.
