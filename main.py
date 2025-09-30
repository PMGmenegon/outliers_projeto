from sqlite import *
from noticias_bbc import get_links
from conteudo import get_content
from gmail_api import send_email
from gemini_api import respond
import datetime


def store_summaries():
    links = get_links()
    noticias = get_content(links)

    create_table()

    header = 'Você é um especialista em resumos de texto que escreve em português do Brasil.\
        Sua única tarefa é resumir o texto que eu fornecer,\
        sem adicionar nenhuma palavra ou frase extra,\
        com um tamanho máximo de 500 caracteres.\
        \n\nresuma o seguinte texto:\n\n'

    for noticia in noticias:
        prompt = header + noticia['title'] + '\n' + noticia['body']

        summary = respond(prompt)

        insert_news(noticia['link'], noticia['date'], noticia['title'], summary)


def send(date):
    email_list = []
    body = 'Este é o resumo automático das mais recentes e mais relevantes notícias do mundo!\n\n\n'

    news = select_news(date=date)

    for piece in news:
        body += piece[3] + '\n\n'
    
    #send_email(email_list, 'Últimas notícias', body)
    print(body)

def main():

    today = datetime.date.today()
    date = int(today.strftime("%Y%m%d"))

    store_summaries()
    send(date)


if __name__ == '__main__':
    main()