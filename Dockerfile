# stdio bridge to Vascue's hosted MCP server.
#
# The real server is the remote streamable-HTTP endpoint
# https://www.vascue.io/mcp/search (public content, no authentication). This
# image exists so stdio-only clients and directory build tests / health checks
# (initialize, tools/list) can talk to it. It holds no data and no secrets.
FROM node:22-alpine

# Pinned so builds are reproducible; bump deliberately.
ARG MCP_REMOTE_VERSION=0.1.38
RUN npm install -g "mcp-remote@${MCP_REMOTE_VERSION}" && npm cache clean --force

# Writable config dir for mcp-remote (it persists OAuth state there; unused for
# this unauthenticated server, but the directory must be writable).
ENV MCP_REMOTE_CONFIG_DIR=/tmp/mcp-remote

USER node
WORKDIR /home/node

LABEL org.opencontainers.image.title="Vascue Public Knowledge Search (MCP stdio bridge)" \
      org.opencontainers.image.source="https://github.com/vascue-io/public-knowledge-search" \
      org.opencontainers.image.url="https://www.vascue.io" \
      org.opencontainers.image.licenses="MIT"

# --transport http-only: the endpoint is streamable HTTP; skip the SSE fallback.
# Directory build specs (e.g. Glama) should use the same command and arguments.
CMD ["mcp-remote", "https://www.vascue.io/mcp/search", "--transport", "http-only"]
