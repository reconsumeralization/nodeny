# config.py

import os
import json


def load_config():
    try:
        return json.load(open("config.json"))
    except FileNotFoundError:
        # Fallback to environment variables if config.json is not found
        return {
            "gemini_api_key": os.getenv("GEMINI_API_KEY", ""),
            "search_url": os.getenv("SEARCH_URL", "https://www.gemini.com/api"),
        }


config = load_config()
