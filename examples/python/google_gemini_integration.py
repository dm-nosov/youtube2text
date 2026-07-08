import requests
from google import genai

client = genai.Client()  # reads GEMINI_API_KEY from the environment


def get_youtube_transcript(video_url: str) -> dict:
    """Fetch the transcript of a YouTube video as plain text."""
    response = requests.get(
        "https://youtube2text.org/api/transcribe",
        params={"url": video_url, "maxChars": 50000},
        headers={"x-api-key": "your_yt2text_key"},
    )
    return response.json()


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Transcribe and summarize: https://www.youtube.com/watch?v=example",
    config=genai.types.GenerateContentConfig(tools=[get_youtube_transcript]),
)

print(response.text)
