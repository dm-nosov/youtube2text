import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY, // or directly pass the key
});

async function main() {
  const response = await anthropic.beta.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 8000,
    messages: [
      {
        role: 'user',
        content: 'Extract and summarize the transcript from https://www.youtube.com/watch?v=example',
      },
    ],
    mcp_servers: [
      {
        name: 'youtube2text',
        type: 'url',
        url: 'https://api.youtube2text.org/mcp',
        authorization_token: 'your_yt2text_key',
      },
    ],
    extra_headers: { 'anthropic-beta': 'mcp-client-2025-04-04' },
  });

  console.log(response.content);
}

main();
