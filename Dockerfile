# Vascue Public Knowledge Search - self-contained MCP server (stdio).
#
# Local BM25 search over the bundled snapshot of vascue.io's public pages in
# content/ (refresh with scripts/fetch_content.py). No network calls at
# runtime, no credentials, public content only. The hosted twin is
# https://www.vascue.io/mcp/search (streamable HTTP).
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY server.py bridge.py ./
COPY content/ content/

USER nobody

LABEL org.opencontainers.image.title="Vascue Public Knowledge Search (MCP server)" \
      org.opencontainers.image.source="https://github.com/vascue-io/public-knowledge-search" \
      org.opencontainers.image.url="https://www.vascue.io" \
      org.opencontainers.image.licenses="MIT"

CMD ["python", "server.py"]
