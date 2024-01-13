# dynamic_gemini_model.py

import google.generativeai as genai


class DynamicGeminiModel:
    def __init__(self, api_key):
        self.api_key = api_key
        self.configure_models()

    def configure_models(self):
        genai.configure(api_key=self.api_key)
        self.text_model = genai.GenerativeModel("gemini-pro")
        self.vision_model = genai.GenerativeModel("gemini-pro-vision")

    def generate_response(self, prompt, is_image_present=False):
        model = self.vision_model if is_image_present else self.text_model
        response = model.generate_content(prompt)
        return response.text

    def adjust_temperature(self, prompt_complexity):
        temperature = 0.4 if prompt_complexity < 5 else 0.9
        return temperature
