import Anthropic from '@anthropic-ai/sdk';
import { BetaRequestMCPServerURLDefinitionParam, BetaMessageParam } from '@anthropic-ai/sdk/resources/beta/index.mjs';

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY, // or directly pass the key
});

async function main() {
  const server: BetaRequestMCPServerURLDefinitionParam = {
    name: 'youtube2text',
    type: 'url',
    url: 'https://api.youtube2text.org/mcp',
    authorization_token: 'your_yt2text_key',
  };

  const message: BetaMessageParam = {
    role: 'user',
    content: 'Extract and summarize the transcript from https://www.youtube.com/watch?v=example',
  };

  const response = await anthropic.beta.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 8000,
    messages: [message],
    mcp_servers: [server],
    extra_headers: { 'anthropic-beta': 'mcp-client-2025-04-04' },
  });

  console.log(response.content);
}

main();
