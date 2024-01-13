# test_text_generation.py

# Assuming DynamicGeminiModel is defined in dynamic_gemini_model.py and is in the same directory
from dynamic_gemini_model import DynamicGeminiModel


# Example test case for text generation
def test_text_generation():
    gemini = DynamicGeminiModel(api_key="AIzaSyCVclBfl40sa6MNlcYE01kf02sZ4uD8sVo")
    prompt = "Write a short my beutiful wife amber"
    response = gemini.generate_response(prompt)
    print("Generated text:", response)


# Run the test function
if __name__ == "__main__":
    test_text_generation()
