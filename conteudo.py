import requests
from bs4 import BeautifulSoup

url = 'https://feeds.bbci.co.uk/news/world/rss.xml'

resposta = requests.get(url) #pega o código fonte da página

if resposta.status_code == 200: # verifica se arequisição foi bem sucedida
    print(" 200, requisicao bem sucedida")
else:
    print( f'Código {resposta.status_code}! Erro na requisicao ' )    

soup = BeautifulSoup(resposta.text, 'lxml-xml') #transformar o xml em algo mais simples de ser lido

itens = soup.find_all('item') # Encontrar todos os links da página

noticias_links = [] 

for item in itens:
    link = item.find('link').text
    if 'video'not in link: #Filtrar apenas os links que parecem ser de notícias escritas
     noticias_links.append(link)
            
noticias_links = list(set(noticias_links)) # Remover duplicatas

for i, link in enumerate(noticias_links, 1):
    print(f'{i}. {link}')
for url in noticias_links:
   response = requests.get(url)
   site = BeautifulSoup(response.content, 'html.parser')
   titulo = site.find('h1')
   data = site.find('time')
   conteudo = site.find('main') or site.find('article')
   conteudo_texto = ''
   if conteudo:
        paragrafos = conteudo.find_all(['p', 'h2', 'h3'])
        conteudo_texto = '\n'.join(p.get_text(strip=True) for p in paragrafos)
   else:
        conteudo_texto = 'Sem conteúdo'
   titulo_texto = titulo.get_text(strip=True) if titulo else 'Sem título'
   data_texto = data.get_text(strip=True) if data else 'Sem data'
   print(f'Manchete: {titulo.text} | Data: {data.text} | Conteúdo: {conteudo.text}')