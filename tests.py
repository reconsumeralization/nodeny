import pytest
from unittest.mock import Mock, patch
from main import main
from gui import GUI
from api_handler import APIHandler
from data_validation import DataValidation, ResponseModel
from utils import setup_logging


def test_main():
    with patch("main.GUI") as mock_gui, patch(
        "main.APIHandler"
    ) as mock_api_handler, patch("main.DataValidation") as mock_data_validation:
        main()
        mock_gui.assert_called_once()
        mock_api_handler.assert_called_once_with(mock_gui)
        mock_data_validation.assert_called_once()


def test_gui():
    gui = GUI()
    assert gui.root.title() == "Generative Language API GUI"
    assert gui.query_entry.get() == ""
    assert gui.response_text.get("1.0", "end-1c") == ""


def test_api_handler():
    gui = GUI()
    api_handler = APIHandler(gui)
    assert api_handler.gui == gui
    assert api_handler.data_validation == None


def test_data_validation():
    data_validation = DataValidation()
    assert isinstance(data_validation, DataValidation)


def test_response_model():
    with pytest.raises(ValueError):
        ResponseModel(predictions=[])

    with pytest.raises(ValueError):
        ResponseModel(predictions=[{"invalid_key": "value"}])

    valid_data = [{"generated_text": "value"}]
    model = ResponseModel(predictions=valid_data)
    assert model.predictions == valid_data


def test_setup_logging(caplog):
    setup_logging()
    assert caplog.record_tuples == [("root", 20, "Logging setup complete.")]


@pytest.mark.asyncio
async def test_make_async_request():
    gui = GUI()
    api_handler = APIHandler(gui)
    api_handler.data_validation = Mock()

    with patch("aiohttp.ClientSession.get") as mock_get:
        mock_get.return_value.__aenter__.return_value.json = Mock(
            return_value={"predictions": [{"generated_text": "value"}]}
        )
        await api_handler.make_async_request("query")
        mock_get.assert_called_once_with("https://api.example.com/generate?query=query")
        api_handler.data_validation.validate_response.assert_called_once_with(
            {"predictions": [{"generated_text": "value"}]}
        )
        api_handler.gui.display_responses.assert_called_once_with(["value"])
