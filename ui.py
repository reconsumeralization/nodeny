# ui.py
import os
from flask import Flask, request, render_template
from multimodal_input import MultimodalInputProcessor
from gemini_vision_pro_api import GeminiVisionProAPI
from response_handler import GeminiResponseHandler

app = Flask(__name__)
gemini_api = GeminiVisionProAPI(api_key=os.getenv('API_KEY'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = MultimodalInputProcessor.process_text_input(request.form['text'])
        image = MultimodalInputProcessor.process_image_input(request.files['image'])
        response = gemini_api.generate_content(text, image)
        analysis = GeminiResponseHandler.analyze_response(response)
        return render_template('result.html', analysis=analysis)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host=os.getenv('HOST', '0.0.0.0'), port=int(os.getenv('PORT', 80)))
