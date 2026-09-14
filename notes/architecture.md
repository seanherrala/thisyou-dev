# Architecture

## Recommended stack

- Graph DB: Neo4j, Memgraph, or Dgraph
- Object storage: R2, S3, or Supabase
- App layer: lightweight TypeScript service and future web frontend

## Core data model

- User nodes
- Post nodes
- Follower/following edges
- Reply/repost/like relations
- Cluster metadata
- Orbit metadata
- Shared pattern signatures

## Functional layers

1. Ingest: pull Bluesky profile, follow graph, and post data
2. Graph: store raw relationships and derived clusters
3. Analysis: detect nests, orbits, repost loops, and ratholes
4. Visualize: generate summary snapshots and shareable outputs
5. Expose: serve the data through an API or frontend

## Design goal

Fast query performance for cluster and orbit detection, without overcomplicating the early build.
