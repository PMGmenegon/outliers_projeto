import requests
from bs4 import BeautifulSoup

def get_links():
   url = 'https://feeds.bbci.co.uk/news/world/rss.xml'

   resposta = requests.get(url) #pega o código fonte da página

   if resposta.status_code == 200: # verifica se arequisição foi bem sucedida
      pass
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

   return noticias_links
