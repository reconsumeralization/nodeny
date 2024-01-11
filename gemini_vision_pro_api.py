# gemini_vision_pro_api.py
import google.generativeai as genai

class GeminiVisionProAPI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)

    def generate_content(self, text, image):
        model = genai.GenerativeModel('gemini-pro-vision')
        return model.generate_content([text, image])
