import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=8000,
    betas=["mcp-client-2025-11-20"],
    mcp_servers=[
        {
            "type": "url",
            "name": "youtube2text",
            "url": "https://youtube2text.org/mcp",
            "authorization_token": "your_yt2text_key",
        }
    ],
    tools=[{"type": "mcp_toolset", "mcp_server_name": "youtube2text"}],
    messages=[
        {
            "role": "user",
            "content": "Extract and summarize the transcript from https://www.youtube.com/watch?v=example",
        }
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
