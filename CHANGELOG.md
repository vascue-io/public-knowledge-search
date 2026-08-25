# Changelog

All notable changes to this repository are recorded here. The hosted endpoint
(`https://www.vascue.io/mcp/search`) is versioned separately by the website
deployment; this file tracks the manifest, bridge image and documentation.

## 1.1.0 - 2026-08-25

- `server.py`: the repo is now a self-contained MCP server - local BM25
  search over a bundled snapshot of vascue.io's public pages (`content/`,
  41 pages, refresh with `scripts/fetch_content.py`). No network calls at
  runtime. Directory releases (Glama) build and run this server locally.
- Dockerfile builds the local server (python:3.12-slim) instead of the
  mcp-remote bridge; CI smoke-tests the Docker image, bare Python, and the
  hosted endpoint separately.
- `bridge.py` + `requirements.txt` (2026-08-23): FastMCP stdio bridge to the
  hosted endpoint, kept for clients that want live content over stdio.

## 1.0.1 - 2026-08-21

- `server.json`: add `repository` so registries can link the source.
- Dockerfile: pin `mcp-remote`, run as the unprivileged `node` user, use
  `--transport http-only`, writable `MCP_REMOTE_CONFIG_DIR`.
- `scripts/smoke.mjs`: stdio smoke test (`initialize` -> `tools/list`).
- GitHub Actions: build the image and run the smoke test on push, PR and weekly.
- README: document the `search` tool and its input schema.

## 1.0.0 - 2026-08-21

- Initial public repository: README, MCP Registry manifest
  (`io.vascue/public-knowledge-search`), `glama.json`, stdio bridge Dockerfile.
