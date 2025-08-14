import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const response = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [{ role: "user", content: "Transcribe and analyze: https://www.youtube.com/watch?v=example" }],
    tools: [
      {
        type: "function",
        function: {
          name: "youtube2text",
          description: "Get the transcript of a YouTube video.",
          parameters: {
            type: "object",
            properties: {
              url: {
                type: "string",
                description: "The URL of the YouTube video.",
              },
            },
            required: ["url"],
          },
        },
      },
    ],
    tool_choice: "auto",
  });

  console.log(response.choices[0]);
}

main();