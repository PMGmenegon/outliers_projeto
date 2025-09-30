
from google import genai

def respond(prompt: str):

    with open('credentials/gemini_key.txt') as file:
        key = file.read()
    
    client = genai.Client(api_key=key)

    response = client.models.generate_content(model='gemini-2.0-flash', contents=prompt)

    return response.text