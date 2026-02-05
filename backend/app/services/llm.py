import requests
import base64
from app.core.config import settings

class LLMService:
    def __init__(self):
        self.api_key = settings.OPENROUTER_API_KEY
        self.base_url = "https://openrouter.ai/api/v1"
        
    def analyze_image(self, image_path: str) -> dict:
        if not self.api_key:
            return {"description": "No API Key provided", "mood": "unknown", "tags": []}

        try:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            prompt = """
            Analyze this image/GIF. Return a JSON object with:
            - description: A short description of the content.
            - mood: The emotional tone (e.g., happy, sombre, energetic).
            - tags: A list of 3-5 keywords.
            """

            data = {
                "model": "google/gemini-2.0-flash-001",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_string}"}}
                        ]
                    }
                ]
            }
            
            response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=data, timeout=60)
            response.raise_for_status()
            result = response.json()
            
            content = result['choices'][0]['message']['content']
            # Simple cleanup validation if LLM returns markdown code block
            if "```json" in content:
                content = content.replace("```json", "").replace("```", "")
            
            import json
            return json.loads(content)
            
        except Exception as e:
            print(f"Error analyzing visuals: {e}")
            return {"description": "Analysis failed", "mood": "unknown", "tags": []}

    def classify_asset(self, filename: str, duration: float, transcription: str = None) -> dict:
        if not self.api_key:
             return {"category": "unknown", "usage_hint": "None"}
             
        try:
            prompt = f"""
            I have a media asset. 
            Filename: "{filename}"
            Duration: {duration} seconds
            Transcription/Text: "{transcription if transcription else 'None'}"
            
            Task: Classify this asset into one of these categories:
            - 'speech': Primary content is spoken word.
            - 'music': Background music, instrumental, or song.
            - 'sfx': Sound effect (laugh, boom, click, etc.).
            - 'visual': If it seems to be a visual overlay (GIF/Image) based on extension (though usually passed as Audio/Video here).
            
            Return a JSON object with:
            - category: 'speech' | 'music' | 'sfx' | 'visual'
            - description: A short, 3-5 word concise description of the sound (e.g., "Upbeat jazz music", "Clown horn honk", "Angry shouting").
            - usage_hint: A short advice on how to use it (e.g., 'Use as background', 'Sync with punchline').
            """
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "google/gemini-2.0-flash-001",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
            
            response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=data, timeout=60)
            response.raise_for_status()
            response.json() # Check for error
            
            content = response.json()['choices'][0]['message']['content']
             # Simple cleanup
            if "```json" in content:
                content = content.replace("```json", "").replace("```", "")
            
            import json
            return json.loads(content)
            
        except Exception as e:
            print(f"Error classifying asset: {e}")
            return {"category": "unknown", "usage_hint": "Manual check required"}
