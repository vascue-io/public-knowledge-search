# Vascue Public Knowledge Search (MCP server)

[![io.vascue/public-knowledge-search on the MCP Registry](https://img.shields.io/badge/MCP%20Registry-io.vascue%2Fpublic--knowledge--search-blue)](https://registry.modelcontextprotocol.io/v0/servers?search=io.vascue)
[![CI](https://github.com/vascue-io/public-knowledge-search/actions/workflows/ci.yml/badge.svg)](https://github.com/vascue-io/public-knowledge-search/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

<a href="https://glama.ai/mcp/servers/vascue-io/public-knowledge-search"><img width="380" height="200" src="https://glama.ai/mcp/servers/vascue-io/public-knowledge-search/badge" alt="Vascue Public Knowledge Search MCP server" /></a>

A [Model Context Protocol](https://modelcontextprotocol.io) server that searches [Vascue](https://www.vascue.io)'s public documentation: healthcare operations, the AI front desk for clinics, provider-side insurance claims automation, Cliniko integration, security, case studies and pricing.

It comes in two equivalent forms:

- **Hosted (always current):** `https://www.vascue.io/mcp/search` - streamable HTTP, no authentication.
- **Self-contained (this repo):** `python server.py` - local BM25 search over a bundled snapshot of the public pages (`content/`, refreshed per release with `scripts/fetch_content.py`). No network calls at runtime, so it also works offline and is what directory-built releases run.

- **Endpoint:** `https://www.vascue.io/mcp/search` (streamable HTTP, no authentication)
- **Server card:** https://www.vascue.io/.well-known/mcp/server-card.json
- **Registry name:** `io.vascue/public-knowledge-search`
- **Operated by:** Vascue Limited (ISO 27001 certified)

> **Public content only.** This server indexes public product and educational pages. Never send patient information, claim documents, clinic credentials or booking requests to it. Agent-based clinic booking is a separate research pilot, not a public API.

## Connect

Any MCP client that speaks streamable HTTP can connect to the endpoint directly.

**Claude Code**

```bash
claude mcp add --transport http vascue-search https://www.vascue.io/mcp/search
```

**Cursor / Claude Desktop / other stdio-only clients** (via [`mcp-remote`](https://www.npmjs.com/package/mcp-remote))

```json
{
  "mcpServers": {
    "vascue-search": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://www.vascue.io/mcp/search"]
    }
  }
}
```

**Self-contained local server** (stdio; bundled snapshot, no network)

```bash
pip install -r requirements.txt
python server.py
```

**Docker** (builds the self-contained server)

```bash
docker build -t vascue-public-knowledge-search .
docker run -i --rm vascue-public-knowledge-search
```

## Tools

One tool, no authentication, read-only.

### `search`

Hybrid (keyword + vector) search over Vascue's public pages. Returns matching excerpts with their canonical `https://www.vascue.io/...` URLs so answers can cite the source.

| Input | Type | Notes |
| --- | --- | --- |
| `query` | `string` (required) | Natural-language question or keywords, e.g. "how does Vascue handle insurance claim pre-authorisation". |
| `ai_search_options.retrieval.retrieval_type` | `"hybrid" \| "vector" \| "keyword"` | Default hybrid. |
| `ai_search_options.retrieval.max_num_results` | `integer` 1–50 | Default 8. |
| `ai_search_options.retrieval.match_threshold` | `number` 0–1 | Default 0.35. |
| `ai_search_options.retrieval.context_expansion` | `integer` 0–3 | Neighbouring chunks to include. |

Query rewriting and reranking are disabled server-side; the server returns source chunks only and never a generated answer, so nothing is presented as a Vascue statement without a citation. Rate limit: 60 requests per minute per client.

Example call:

```json
{ "name": "search", "arguments": { "query": "Cliniko integration for AI front desk" } }
```

The endpoint is backed by a Cloudflare AI Search instance over the approved public Markdown export of vascue.io (the service descriptor at https://www.vascue.io/.well-known/ai-search.json states what is and is not indexed).

## Development

```bash
docker build -t vascue-public-knowledge-search .
node scripts/smoke.mjs docker run -i --rm vascue-public-knowledge-search   # initialize -> tools/list
node scripts/smoke.mjs npx -y mcp-remote https://www.vascue.io/mcp/search --transport http-only
```

CI runs the same build and smoke test on every push and weekly, so the badge above doubles as an endpoint health indicator.

### Directory build specs

Two equivalent stdio bridges are kept in this repo so a directory can build the server on whichever runtime it offers. Neither needs environment variables.

| Runtime | Build steps | CMD |
| --- | --- | --- |
| Node (`Dockerfile`) | `["npm install -g mcp-remote@0.1.38"]` | `["mcp-remote", "https://www.vascue.io/mcp/search", "--transport", "http-only"]` |
| Python 3.12+ (`bridge.py`) | `["uv pip install --system -r requirements.txt"]` (or plain `pip install -r requirements.txt` where pip exists) | `["python", "bridge.py"]` |

Note for Glama specifically: its build image provides Python through `uv`, which ships no `pip` shim — use the `uv pip install --system` form there. Node and npm are also preinstalled in Glama's image, so the Node row works as-is.

```bash
pip install -r requirements.txt
SMOKE_CALL_QUERY="Cliniko integration" node scripts/smoke.mjs python server.py   # local server
node scripts/smoke.mjs python bridge.py                                          # stdio bridge to the hosted endpoint
python scripts/fetch_content.py                                                  # refresh the content/ snapshot
```

## Other machine-readable surfaces

- `https://www.vascue.io/llms.txt`
- `https://www.vascue.io/openapi.json` (public, read-only content API)
- `https://www.vascue.io/.well-known/agent-skills/index.json` (agent skills; also at [vascue-io/skills](https://github.com/vascue-io/skills))

## Licence

This repository (README, manifest, Dockerfile) is MIT licensed. The content served by the endpoint is Vascue's public website content.
