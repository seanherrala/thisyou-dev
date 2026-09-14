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
python -m pip install -e .
python -m thisyou.cli
```

## Current status

This repository is intentionally scaffolded as a minimal starting point. The next steps are to define the first user/post graph model, ingest pipeline, and analysis pass.
