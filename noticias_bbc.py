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