import OpenAI from "openai";

const openai = new OpenAI(); // reads OPENAI_API_KEY from the environment

async function main(): Promise<void> {
  const response = await openai.responses.create({
    model: "gpt-5",
    tools: [
      {
        type: "mcp",
        server_label: "youtube2text",
        server_url: "https://youtube2text.org/mcp",
        headers: { "x-api-key": "your_yt2text_key" },
        require_approval: "never",
      },
    ],
    input: "Transcribe and analyze: https://www.youtube.com/watch?v=example",
  });

  console.log(response.output_text);
}

main();
