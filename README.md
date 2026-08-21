# Vascue Public Knowledge Search (MCP server)

[![io.vascue/public-knowledge-search on the MCP Registry](https://img.shields.io/badge/MCP%20Registry-io.vascue%2Fpublic--knowledge--search-blue)](https://registry.modelcontextprotocol.io/v0/servers?search=io.vascue)

A remote [Model Context Protocol](https://modelcontextprotocol.io) server that searches [Vascue](https://www.vascue.io)'s public documentation: healthcare operations, the AI front desk for clinics, provider-side insurance claims automation, Cliniko integration, security, case studies and pricing.

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

**Docker** (the same stdio bridge, used by directory health checks)

```bash
docker build -t vascue-public-knowledge-search .
docker run -i --rm vascue-public-knowledge-search
```

## Tools

The server exposes a search tool over Vascue's public pages and returns page excerpts with their canonical `https://www.vascue.io/...` URLs, so answers can cite the source. Call `tools/list` after `initialize` for the current schema.

## Other machine-readable surfaces

- `https://www.vascue.io/llms.txt`
- `https://www.vascue.io/openapi.json` (public, read-only content API)
- `https://www.vascue.io/.well-known/agent-skills/index.json` (agent skills; also at [vascue-io/skills](https://github.com/vascue-io/skills))

## Licence

This repository (README, manifest, Dockerfile) is MIT licensed. The content served by the endpoint is Vascue's public website content.
