import vertexai
import PIL
from vertexai.preview.generative_models import GenerativeModel, Part


vertexai.configure(api_key= "AIzaSyA1sMAt7m0ft40zgJRS81ggY1qKM5MX1s0")


def generate_text(project_id: str, location: str) -> str:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    # Load the model
    multimodal_model = GenerativeModel("gemini-1.0-pro-vision")
    # Query the model
    response = multimodal_model.generate_content(
        [
            # Add an example image
            Part.from_uri(
                "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
            ),
            # Add an example query
            "what is shown in this image?",
        ]
    )





    PIL.Image.open("gs://generativeai-downloads/images/scones.jpg").show()
    print(response)
    return response.text


generate_text("mirs-1697647230921", "us-central1")