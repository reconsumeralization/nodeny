import aiohttp
import logging
from urllib.parse import quote
from data_validation import DataValidation  # Re-import DataValidation


class APIHandler:
    """
    This class handles API requests and responses.
    """

    def __init__(self, gui=None):
        """
        Initialize the APIHandler with a GUI instance.
        """
        self.gui = gui
        self.data_validation = DataValidation()

    async def make_async_request(self, query: str):
        """
        Make an asynchronous request to the API with the given query.
        """
        async with aiohttp.ClientSession() as session:
            try:
                url = "https://api.example.com/generate?query=" f"{quote(query)}"
                async with session.get(url) as resp:
                    data = await resp.json()
                    self.data_validation.validate_response(
                        data
                    )  # Validate the response
                    responses = self.parse_response(data)
                    self.gui.display_responses(responses)
                    return responses  # Ensure data is always a list or iterable
            except aiohttp.ClientError as e:
                logging.error(f"Request failed: {e}")
                # Handle the error appropriately
                return []  # Return an empty list in case of an error
            except ValueError as e:
                logging.error(f"Validation error: {e}")
                # Handle the validation error appropriately
                return []  # Return an empty list in case of an error

    def parse_response(self, data: dict) -> list:
        """
        Parse the response data and return a list of generated texts.
        """
        responses = [item["generated_text"] for item in data["predictions"]]
        return responses
