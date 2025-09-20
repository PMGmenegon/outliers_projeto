
from google import genai


def summarize(text: str):
    prompt = f'Gere um resumo dessa notícia usando no máximo 100 palavras:\n{text}'

    return respond(prompt)

def respond(prompt: str):

    with open('credentials/gemini_key.txt') as file:
        key = file.read()
    
    client = genai.Client(api_key=key)

    response = client.models.generate_content(model='gemini-2.0-flash', contents=prompt)

    return response.text