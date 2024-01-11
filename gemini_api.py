# gemini_api.py

import google.generativeai as genai


def configure_gemini_model(model_name, api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name=model_name)
