import google.generativeai as genai
import requests

genai.configure(api_key="your_gemini_key")

def get_youtube_transcription(video_url: str) -> dict:
    """Fetch YouTube video transcription via API."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer your_yt2text_key"
    }
    
    response = requests.post(
        "https://api.youtube2text.org/mcp",
        headers=headers,
        json={"url": video_url}
    )
    
    return response.json() if response.ok else {"error": str(response.text)}

model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    tools=[get_youtube_transcription]
)

chat = model.start_chat(enable_automatic_function_calling=True)
response = chat.send_message("Transcribe: https://www.youtube.com/watch?v=example")

print(response.text)
