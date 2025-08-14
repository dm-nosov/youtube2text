import anthropic
from anthropic.types.beta import BetaRequestMCPServerURLDefinitionParam, BetaMessageParam

client = anthropic.Anthropic(api_key="your_anthropic_key")

server = BetaRequestMCPServerURLDefinitionParam(
    name="youtube2text",
    type="url",
    url="https://api.youtube2text.org/mcp",
    authorization_token="your_yt2text_key"
)

message = BetaMessageParam(
    role="user", 
    content="Extract and summarize the transcript from https://www.youtube.com/watch?v=example"
)

response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=8000,
    messages=[message],
    mcp_servers=[server],
    extra_headers={"anthropic-beta": "mcp-client-2025-04-04"}
)

print(response.content)
