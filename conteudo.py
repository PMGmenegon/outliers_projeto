import requests
from bs4 import BeautifulSoup
import datetime

def get_content(noticias_links):
    today = datetime.date.today()
    date = int(today.strftime("%Y%m%d"))

    noticias = []
    for url in noticias_links:
        noticia = {'date': date, 'link': url}
        response = requests.get(url)
        site = BeautifulSoup(response.content, 'html.parser')
        conteudo = site.find('main') or site.find('article')
        if conteudo:
            paragrafos = conteudo.find_all(['p', 'h2', 'h3'])
            noticia['body'] = '\n'.join(p.get_text(strip=True) for p in paragrafos)
        else:
            continue
        titulo = site.find('h1')
        noticia['title'] = titulo.get_text(strip=True) if titulo else 'Sem título'
        noticias.append(noticia)
    return noticias