# Changelog

All notable changes to this repository are recorded here. The hosted endpoint
(`https://www.vascue.io/mcp/search`) is versioned separately by the website
deployment; this file tracks the manifest, bridge image and documentation.

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
