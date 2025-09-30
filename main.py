from sqlite import *
from noticias_bbc import get_links
from conteudo import get_content
from gmail_api import send_email
from gemini_api import respond

def main():
    email_list = []
    links = get_links()
    noticias = get_content(links)

    create_table()

    prompt = 'Selecione as cinco notícias mais relevantes entre as seguintes notícias e responda\
        única e exclusivamente com um texto de aproximadamente 3000 caracteres\
        contendo um resumo das cinco notícias mais relevantes traduzidas para pt-br:\n\n\n'

    bodys = []
    for noticia in noticias:
        #insert_news(noticia['link'], noticia['date'], noticia['title'], noticia['body'])
        bodys.append(noticia['title'] + '\n' + noticia['body'] + '\n\n\n')
    
    prompt += ''.join(bodys)

    response = respond(prompt)

    send_email(email_list, 'Últimas Notícias', response)

if __name__ == '__main__':
    main()
