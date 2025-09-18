
from google import genai


def summarize(text):
    prompt = f'Gere um resumo dessa notícia usando no máximo 100 palavras:\n{text}'

    # Set environment variable GEMINI_API_KEY as the api key beforehand
    client = genai.Client()

    response = client.models.generate_content(model='gemini-2.0-flash', contents=prompt)

    return response.text