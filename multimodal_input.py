# multimodal_input.py
import PIL.Image
import io


class MultimodalInputProcessor:
    @staticmethod
    def process_text_input(text):
        # Process and return text input
        return text

    @staticmethod
    def process_image_input(image_path):
        # Open and process the image
        with open(image_path, "rb") as img_file:
            return PIL.Image.open(io.BytesIO(img_file.read()))
