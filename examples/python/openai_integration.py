from openai import OpenAI
from openai.types.responses.tool_param import Mcp

client = OpenAI(api_key="your_openai_key")

mcp_tool = Mcp(
    type="mcp",
    server_label="youtube2text",
    server_url="https://api.youtube2text.org/mcp",
    require_approval="never",
    headers={"Authorization": "Bearer your_yt2text_key"}
)

response = client.responses.create(
    model="gpt-4.1",
    tools=[mcp_tool],
    input="Transcribe and analyze: https://www.youtube.com/watch?v=example"
)

print(response.output_text)
