import click
from api_handler import APIHandler
from data_validation import DataValidation
from utils import setup_logging


@click.group()
def cli_tool():
    pass


@cli_tool.command()
@click.argument("query")
async def generate(query):  # Added async keyword here
    """Generate text based on the provided query."""
    # Setup logging
    setup_logging()

    # Create instances of the classes
    api_handler = APIHandler()
    data_validation = DataValidation()

    # Connect the DataValidation to APIHandler
    api_handler.data_validation = data_validation

    # Make the API request and print the responses
    responses = await api_handler.make_async_request(query)  # Added await keyword here
    if responses is not None:  # Added check to ensure responses is iterable
        for response in responses:
            print(response)


if __name__ == "__main__":
    cli_tool()
