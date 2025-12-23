from google import genai
client = genai.Client(api_key="AIzaSyCMop6JY7MwbTQjoj4xT8SbW3xXo-X1mRE")

def get_response(text):
    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=text
    )
    return response.text
