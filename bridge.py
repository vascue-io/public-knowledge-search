"""stdio bridge to Vascue's hosted MCP server (streamable HTTP, public content)."""
from fastmcp import FastMCP

FastMCP.as_proxy(
    "https://www.vascue.io/mcp/search",
    name="vascue-public-knowledge-search",
).run()
