# YouTube2Text - Video Transcription API

A powerful text extraction service that converts YouTube video content into clean, timestampless transcripts for content analysis, research, and processing workflows.

## Overview

YouTube2Text transforms YouTube videos into readable text by removing subtitle timing markers and metadata, delivering pure content suitable for:

- Content analysis and insights
- Text summarization workflows  
- Research and documentation
- Content generation pipelines
- Natural language processing tasks

## Quick Start

Begin with a demo API key from [https://api.youtube2text.org](https://api.youtube2text.org). For consistent access and higher usage limits, upgrade to a subscription plan.

## API Reference

**Base URL**: `https://api.youtube2text.org`  
**Transcription Endpoint**: `/transcribe`

### Request Format

Send POST requests with these parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Complete YouTube video URL |
| `maxChars` | number | No | Character limit (default: 150,000) |

### Authentication

Include your API key in the request header:
```
x-api-key: YOUR_API_KEY
```

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
- `RATE_LIMIT_EXCEEDED`: Quota or rate limit reached
- `INTERNAL_ERROR`: Server-side issue

## Examples

This directory contains examples of how to use the YouTube2Text API with different AI models and in different programming languages.

### Python

*   [Anthropic Claude Integration](./examples/python/anthropic_claude_integration.py)
*   [OpenAI Integration](./examples/python/openai_integration.py)
*   [Google Gemini Integration](./examples/python/google_gemini_integration.py)

### JavaScript

*   [Anthropic Claude Integration](./examples/javascript/anthropic_claude_integration.js)
*   [OpenAI Integration](./examples/javascript/openai_integration.js)
*   [Google Gemini Integration](./examples/javascript/google_gemini_integration.js)

### TypeScript

*   [Anthropic Claude Integration](./examples/typescript/anthropic_claude_integration.ts)
*   [OpenAI Integration](./examples/typescript/openai_integration.ts)
*   [Google Gemini Integration](./examples/typescript/google_gemini_integration.ts)


## Automation Integration

### Workflow Automation

The API integrates with popular automation platforms:

- **Zapier**: Connect via MCP integration for triggered workflows
- **n8n**: Use HTTP request nodes or MCP connectors for process automation
- **Make (Integromat)**: HTTP modules for video processing pipelines

### Example Workflow Ideas

1. **Content Pipeline**: YouTube → Transcription → Summary → Social Media Posts
2. **Research Automation**: Video URLs → Transcripts → Analysis → Report Generation  
3. **Content Monitoring**: Channel Watching → New Videos → Auto-transcription → Alerts

## Response Examples

### Successful Response

```json
{
  "result": {
    "videoId": "dQw4w9WgXcQ",
    "title": "Rick Astley - Never Gonna Give You Up (Official Video)",
    "pubDate": "2009-10-25T07:57:33-07:00",
    "content": "We're no strangers to love You know the rules and so do I...",
    "contentSize": 1337,
    "truncated": false
  }
}
```

### Error Response

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Monthly quota exceeded",
    "status": 429,
    "retryAfterSeconds": 3600,
    "details": "Upgrade plan for higher limits"
  }
}
```

## Best Practices

- Store API keys securely using environment variables
- Implement proper error handling for all status codes
- Respect rate limits and implement retry logic with exponential backoff
- Cache transcripts locally when possible to avoid redundant API calls
- Monitor usage to stay within quota limits
- Use appropriate `maxChars` limits for your use case

## Support

For additional examples, troubleshooting, and advanced integration patterns, visit the project repository or API documentation.