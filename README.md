# YouTube2Text - Video Transcription API

A text extraction service that converts YouTube video content into clean, timestampless transcripts for content analysis, research, and processing workflows. Available as a REST API and as an MCP server for AI agents.

## Overview

YouTube2Text transforms YouTube videos into readable text by removing subtitle timing markers and metadata, delivering pure content suitable for:

- Content analysis and insights
- Text summarization workflows
- Research and documentation
- Content generation pipelines
- AI agent and RAG pipelines

## Quick Start

```bash
# Get the free shared demo key (no account, 5 videos/month per IP)
curl -s https://youtube2text.org/api/demo-key
# -> {"success":true,"apiKey":"yt_..."}

# Fetch a transcript
curl -s "https://youtube2text.org/api/transcribe?url=https://www.youtube.com/watch?v=VIDEO_ID&maxChars=5000" \
  -H "x-api-key: yt_YOUR_KEY"
```

For your own key and higher limits, sign in with Google at [youtube2text.org/app/keys](https://youtube2text.org/app/keys).

## API Reference

**Base URL**: `https://youtube2text.org`
**Transcription Endpoint**: `/api/transcribe` (GET or POST)

Complete machine-readable reference: [youtube2text.org/api.md](https://youtube2text.org/api.md) (index: [/llms.txt](https://youtube2text.org/llms.txt)). Existing integrations using `https://api.youtube2text.org` continue to work.

### Request Format

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Any YouTube URL form (watch, `youtu.be`, Shorts, embed) or a bare 11-character video ID |
| `maxChars` | number | No | Character limit (default and max: 150,000) |

### Authentication

Include your API key in the request header:
```
x-api-key: YOUR_API_KEY
```
`Authorization: Bearer YOUR_API_KEY` is also accepted.

### HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Transcription successful |
| 400 | Invalid request parameters |
| 401 | Authentication failed |
| 404 | Video or transcript not found |
| 429 | Rate limit exceeded |
| 500 | Server error |

### Error Types

- `VALIDATION_ERROR`: Parameter validation failed
- `UNAUTHORIZED`: Invalid API credentials
- `VIDEO_NOT_FOUND`: YouTube video unavailable
- `TRANSCRIPT_UNAVAILABLE`: No captions available
- `INVALID_URL`: Malformed video URL
- `RATE_LIMIT_EXCEEDED`: Quota or rate limit reached (`retryAfterSeconds` included)
- `YOUTUBE_ERROR`: Upstream YouTube failure, retry later
- `INTERNAL_ERROR`: Server-side issue

All error responses include a `docsUrl` field pointing at the API reference.

## MCP Server (AI agents)

The MCP server at `https://youtube2text.org/mcp` (streamable HTTP) exposes a `transcribe_video(url, maxChars?)` tool. OAuth 2.1 is supported, so clients like claude.ai connect without manual key handling; an API key header works for everything else.

- **claude.ai**: Settings → Connectors → Add custom connector → `https://youtube2text.org/mcp` → sign in with Google and click Allow.
- **Claude Code**: `claude mcp add --transport http youtube2text https://youtube2text.org/mcp`
- **Claude API**: add `{"type": "url", "url": "https://youtube2text.org/mcp", "name": "youtube2text", "authorization_token": "YOUR_API_KEY"}` to `mcp_servers`.
- **OpenAI Responses API**: add `{"type": "mcp", "server_label": "youtube2text", "server_url": "https://youtube2text.org/mcp", "headers": {"x-api-key": "YOUR_KEY"}, "require_approval": "never"}` to `tools`.

Integration guides and recipes: [youtube2text.org/blog](https://youtube2text.org/blog).

## Examples

This directory contains examples of how to use the YouTube2Text API with different AI models and in different programming languages.

### Python

*   [Anthropic Claude Integration](./examples/python/anthropic_claude_integration.py)
*   [OpenAI Integration](./examples/python/openai_integration.py)
*   [Google Gemini Integration](./examples/python/google_gemini_integration.py)

### JavaScript

*   [Anthropic Claude Integration](./examples/javascript/anthropic_claude_integration.js)
*   [OpenAI Integration](./examples/javascript/openai_integration.js)

### TypeScript

*   [Anthropic Claude Integration](./examples/typescript/anthropic_claude_integration.ts)
*   [OpenAI Integration](./examples/typescript/openai_integration.ts)
