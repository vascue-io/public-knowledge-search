# stdio bridge to Vascue's hosted MCP server. The real server is the remote
# streamable-HTTP endpoint; this image exists so stdio-only clients and
# directory health checks (initialize / tools/list) can talk to it.
FROM node:22-alpine
RUN npm install -g mcp-remote@latest && npm cache clean --force
ENV VASCUE_MCP_URL=https://www.vascue.io/mcp/search
ENTRYPOINT ["sh", "-c", "exec mcp-remote \"$VASCUE_MCP_URL\""]
