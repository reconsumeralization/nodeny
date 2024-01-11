# config.py
import os
import json


def load_config():
    try:
        return json.load(open('config.json'))
    except FileNotFoundError:
        # Fallback to environment variables if config.json is not found
        return {
            'gemini_api_key': os.getenv('GEMINI_API_KEY', ''),
            'search_url': os.getenv('SEARCH_URL', 'https://www.gemini.com/api')
        }


config = load_config()

# gemini_api.py
import google.generativeai as genai


def configure_gemini_model(model_name, api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name=model_name)


# data_store.py
def adjust_data_recursively(data, condition_func, adjust_func):
    if isinstance(data, dict):
        return {k: adjust_data_recursively(v, condition_func, adjust_func) for k, v in data.items()}
    elif isinstance(data, list):
        return [adjust_data_recursively(item, condition_func, adjust_func) for item in data]
    return adjust_func(data) if condition_func(data) else data


# main.py
import argparse
from config import config
from gemini_api import configure_gemini_model
from data_store import adjust_data_recursively
from gui import GUI
from ui import app


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Run the GUI or web application.')
    parser.add_argument('--interface', choices=['gui', 'web'], default='gui',
                        help='the interface to run (default: gui)')
    args = parser.parse_args()

    # Model selection based on user input or other criteria
    model_name = 'models/gemini-pro-vision'  # Example model
    gemini_model = configure_gemini_model(model_name, config['gemini_api_key'])

    # Example data store
    data_store = {
        "example_key": "dark_string",
        "nested": {"inner_key": "another_dark_string"}
    }

    # Define adjustment logic
    def should_adjust(value):
        return isinstance(value, str) and "dark" in value

    def adjust_value(value):
        return f"adjusted_{value}"

    # Adjust data store
    adjusted_data = adjust_data_recursively(data_store, should_adjust, adjust_value)
    print("Adjusted Data:", adjusted_data)

    # Run the selected interface
    if args.interface == 'gui':
        try:
            gui = GUI()
            gui.run()
        except Exception as e:
            print(f"Failed to start GUI: {e}")
    else:
        try:
            app.run(debug=True)
        except Exception as e:
            print(f"Failed to start web application: {e}")


if __name__ == "__main__":
    main()
