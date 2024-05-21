""" Problema Prático 11.1

Escreva o método news() que aceita um URL de um site Web de notícias e uma lista de tópicos de notícias (ou seja, strings) e calcula o número de ocorrências de cada tópico nas notícias.

>>> news('http://bbc.co.uk',['economy','climate','education'])

economy appears 3 times.

climate appears 3 times.

education appears 1 times. """
from urllib.request import urlopen

def news(url, topics):
    response = urlopen(url)
    html = response.read()
    content = html.decode().lower()
    for topic in topics:
        n = content.count(topic)
        print('{} appears {} times.'.format(topic,n))

news('http://bbc.co.uk', ['economy','climate','education'])