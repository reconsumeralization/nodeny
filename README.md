# Generative Language API GUI

This project is a Pythonic GUI application that integrates Google's Generative Language API with function calling. It presents candidate outputs for user selection and incorporates modern Python practices. The application focuses on user interaction for model refinement.

## Features

- Asynchronous API requests using `asyncio`
- File path management using `pathlib`
- Data processing using comprehensions
- Function declarations using `Enum`
- Caching API responses using `functools.lru_cache`
- Data validation using `Pydantic`
- Code formatting using `Flake8/Black`
- Static type checking using `Mypy`
- Efficient data handling using generators
- Testing using `pytest`
- Database interactions using `SQLAlchemy`
- CLI tool using `Click`
- Utilization of modern Python features (3.8+)
- Functional programming techniques
- Comprehensive exception handling
- Dependency management and packaging using `poetry/pipenv`

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

To start the application, run:

```bash
python main.py
```

For CLI usage, run:

```bash
python main.py --help
```

## Project Structure

- `main.py`: The main entry point of the application.
- `gui.py`: Contains the `GUI` class for building the user interface.
- `api_handler.py`: Contains the `APIHandler` class for handling API interactions.
- `data_validation.py`: Contains the `DataValidation` class for validating user inputs and API responses.
- `utils.py`: Contains utility functions such as `setup_logging`.
- `tests.py`: Contains tests for the application.
- `cli.py`: Contains the `cli_tool` for CLI usage.
- `requirements.txt`: Contains the required dependencies for the project.

## Code Snippets

Here are some code snippets from the project:

### main.py

```python
import asyncio
from gui import GUI
from api_handler import APIHandler
from data_validation import DataValidation
from utils import setup_logging
from cli import cli_tool

def main():
    # Setup logging
    setup_logging()

    # Create instances of the classes
    gui = GUI()
    api_handler = APIHandler()
    data_validation = DataValidation()

    # Connect the GUI and APIHandler
    gui.api_handler = api_handler
    api_handler.gui = gui

    # Connect the DataValidation to APIHandler
    api_handler.data_validation = data_validation

    # Run the GUI
    gui.run()

if __name__ == "__main__":
    # Check if CLI arguments are provided
    if len(sys.argv) > 1:
        cli_tool()
    else:
        main()
```

### gui.py

```python
import asyncio
from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, END
from api_handler import APIHandler

class GUI:
    def __init__(self):
        self.api_handler = None
        self.root = Tk()
        self.root.title("Generative Language API GUI")
        self.query_entry = Entry(self.root, width=50)
        self.submit_button = Button(self.root, text="Submit", command=self.handle_user_input)
        self.response_text = Text(self.root, width=50, height=10)
        self.scrollbar = Scrollbar(self.root, command=self.response_text.yview)
        self.response_text['yscrollcommand'] = self.scrollbar.set

    def run(self):
        self.query_entry.pack()
        self.submit_button.pack()
        self.response_text.pack(side="left", fill="y")
        self.scrollbar.pack(side="right", fill="y")
        self.root.mainloop()

    def handle_user_input(self):
        query = self.query_entry.get()
        asyncio.run(self.api_handler.make_async_request(query))

    def display_responses(self, responses):
        self.response_text.delete(1.0, END)
        for response in responses:
            self.response_text.insert(END, response + "\n")
```

### api_handler.py

```python
import asyncio
import aiohttp
from functools import lru_cache
from data_validation import DataValidation

class APIHandler:
    def __init__(self):
        self.gui = None
        self.data_validation = None

    @lru_cache(maxsize=128)
    async def make_async_request(self, query):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.example.com/generate?query={query}') as resp:
                data = await resp.json()
                self.data_validation.validate_response(data)
                responses = self.parse_response(data)
                self.gui.display_responses(responses)

    def parse_response(self, data):
        responses = [item['generated_text'] for item in data['predictions']]
        return responses
```

### data_validation.py

```python
from pydantic import BaseModel, ValidationError, validator
from typing import List, Dict, Any

class ResponseModel(BaseModel):
    predictions: List[Dict[str, Any]]

    @validator('predictions')
    def check_predictions(cls, predictions):
        if not predictions:
            raise ValueError('No predictions found in the response')
        for prediction in predictions:
            if 'generated_text' not in prediction:
                raise ValueError('Invalid prediction format')
        return predictions
```

### utils.py

```python
import logging
from functools import lru_cache

def setup_logging():
    logging.basicConfig(level=logging.INFO,
```
