# Project brief

## Project name

thisyou

Domain: thisyou.dev
Handle: @thisyou.dev

## Purpose

thisyou is a Bluesky-native visualization tool that reveals user patterns, clusters, repost loops, nests, ratholes, and interaction orbits. It lets the picture speak for itself.

## Mission

To map, visualize, and summarize Bluesky users in a way that exposes patterns without moralizing. The tool should help surface suspicious behavior and contextualize normal behavior.

## Tone

Observational, perceptive, curious, lightly bratty, never smug, never moralizing.

## Architecture direction

- Graph database for users, posts, edges, cluster metadata, orbit structures, and pattern signatures
- Object storage for snapshots, cached Bluesky responses, and heavy JSON blobs
- Visualization layer that turns graph data into readable, shareable summaries
- Analysis layer that identifies loops, nests, orbits, and interaction clusters

## Development philosophy

Build small, visual, testable parts. Let the visualization do the talking. Keep the tone consistent. Avoid editorial judgment.

## One-line summary

thisyou.dev is a Bluesky-native visualization engine that quietly reveals user patterns by letting the picture speak.
