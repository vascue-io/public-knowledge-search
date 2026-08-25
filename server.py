#!/usr/bin/env python3
"""Vascue Public Knowledge Search - self-contained MCP server.

Runs entirely locally over the bundled snapshot in content/ (Markdown twins of
vascue.io's public pages; refresh with scripts/fetch_content.py). BM25 ranking,
no network calls, no credentials, public content only.

The hosted twin of this server is https://www.vascue.io/mcp/search.
"""
from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Annotated

from pydantic import Field

from fastmcp import FastMCP

CONTENT_DIR = Path(__file__).resolve().parent / "content"
CHUNK_TARGET_CHARS = 1200
TOKEN_PATTERN = re.compile(r"[a-z0-9]+")
FRONTMATTER_PATTERN = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)


def tokenize(text: str) -> list[str]:
    return TOKEN_PATTERN.findall(text.lower())


def parse_page(raw: str) -> tuple[str, str, str]:
    """Return (title, canonical_url, body) from a Markdown twin."""
    title, canonical, body = "", "", raw
    match = FRONTMATTER_PATTERN.match(raw)
    if match:
        body = raw[match.end():]
        for line in match.group(1).splitlines():
            key, _, value = line.partition(":")
            value = value.strip().strip('"')
            if key.strip() == "title":
                title = value
            elif key.strip() == "canonical":
                canonical = value
    return title, canonical, body


def split_chunks(body: str) -> list[str]:
    """Split on headings, then pack paragraphs into ~CHUNK_TARGET_CHARS pieces."""
    sections = re.split(r"(?m)^(?=#{1,3} )", body)
    chunks: list[str] = []
    for section in sections:
        paragraphs = [p.strip() for p in section.split("\n\n") if p.strip()]
        current = ""
        for paragraph in paragraphs:
            if current and len(current) + len(paragraph) > CHUNK_TARGET_CHARS:
                chunks.append(current)
                current = paragraph
            else:
                current = f"{current}\n\n{paragraph}" if current else paragraph
        if current:
            chunks.append(current)
    return [c for c in chunks if len(tokenize(c)) >= 5]


class Index:
    """Small BM25 index over the bundled pages."""

    def __init__(self, content_dir: Path) -> None:
        self.chunks: list[dict] = []
        for path in sorted(content_dir.glob("*.md")):
            title, canonical, body = parse_page(path.read_text(encoding="utf-8"))
            for text in split_chunks(body):
                self.chunks.append({"url": canonical, "title": title, "text": text, "tokens": tokenize(f"{title} {text}")})
        self.doc_frequency: dict[str, int] = {}
        for chunk in self.chunks:
            for token in set(chunk["tokens"]):
                self.doc_frequency[token] = self.doc_frequency.get(token, 0) + 1
        total = sum(len(c["tokens"]) for c in self.chunks)
        self.average_length = total / len(self.chunks) if self.chunks else 1.0

    def search(self, query: str, limit: int) -> list[dict]:
        query_tokens = tokenize(query)
        if not query_tokens or not self.chunks:
            return []
        n = len(self.chunks)
        k1, b = 1.5, 0.75
        scored: list[tuple[float, dict]] = []
        for chunk in self.chunks:
            length = len(chunk["tokens"])
            counts: dict[str, int] = {}
            for token in chunk["tokens"]:
                counts[token] = counts.get(token, 0) + 1
            score = 0.0
            for token in query_tokens:
                frequency = counts.get(token, 0)
                if not frequency:
                    continue
                df = self.doc_frequency.get(token, 0)
                idf = math.log(1 + (n - df + 0.5) / (df + 0.5))
                score += idf * (frequency * (k1 + 1)) / (frequency + k1 * (1 - b + b * length / self.average_length))
            if score > 0:
                scored.append((score, chunk))
        scored.sort(key=lambda pair: pair[0], reverse=True)
        top = scored[:limit]
        best = top[0][0] if top else 1.0
        return [
            {"url": c["url"], "title": c["title"], "score": round(s / best, 4), "text": c["text"]}
            for s, c in top
        ]


INDEX = Index(CONTENT_DIR)

mcp = FastMCP(
    name="vascue-public-knowledge-search",
    version="1.1.0",
    instructions=(
        "Local search over a bundled snapshot of Vascue's public website. Public content only: "
        "never send patient information, claim documents, clinic credentials or booking requests."
    ),
)


@mcp.tool(
    annotations={
        "title": "Search Vascue's public documentation",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
def search(
    query: Annotated[str, Field(min_length=1, description='What to look for, as a natural-language question or keywords. 3-15 words works best; one topic per call (split multi-part questions into separate calls). Examples: "how does claims pre-authorisation work", "Cliniko integration", "pricing for physiotherapy clinics". Matching is keyword-based (BM25), so prefer concrete product terms over abstract phrasing.')],
    max_num_results: Annotated[int, Field(ge=1, le=50, description="Maximum excerpts to return, 1-50 (default 8). Use 3-5 for a quick factual answer, 8 (default) for typical questions, 15+ only for a broad research sweep across many pages; larger values return progressively less relevant chunks.")] = 8,
) -> dict:
    """Keyword (BM25) search over a bundled snapshot of vascue.io's public pages: healthcare-operations guides, the AI front desk for clinics, provider-side insurance-claims automation, Cliniko and Nookal integration, security and compliance pages, case studies, pricing and blog posts.

Use it to answer questions about what Vascue offers, how its products work and what it has published. One topic per call; cite the returned page URL for every excerpt you use.

Returns {"chunks": [...]} ordered by relevance; each chunk has url (the canonical https://www.vascue.io/... page), title, score (0-1 relative to the best match) and text (a Markdown excerpt). An empty list means the snapshot does not mention the topic - say so rather than guessing. The index is a point-in-time copy of the public site; https://www.vascue.io/mcp/search is the always-current hosted twin.

Runs fully locally: read-only, idempotent, no network calls, no authentication. Public content only: never send patient information, claim documents, clinic credentials or booking requests. It cannot book appointments or look up clinic data."""
    return {"chunks": INDEX.search(query, max_num_results)}


if __name__ == "__main__":
    mcp.run()
