from google import genai
from google.genai import types
import os

class AIService:
    def __init__(self):
        # API Key is pulled from environment variables for security
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    async def analyze_image_bytes(self, image_bytes: bytes, mime_type: str):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
                "Identify the objects in this image and provide a brief description."
            ]
        )
        return response.text