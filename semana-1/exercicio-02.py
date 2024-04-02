""" Problema Prático 3.15

Implemente a função olimpíadas(t), que faz com que a tartaruga t desenhe os anéis olímpicos mostrados a seguir. Use a função jump() do módulo ch3. Você conseguirá obter a imagem desenhada executando:

>>> import turtle

>>> s = turtle.Screen()

>>> t = turtle.Turtle()

>>> olimpíadas(t) """

import turtle


def jump(t, x, y):
    # Levanta a caneta e move para a posição (x, y) sem desenhar
    t.penup()
    t.goto(x,y)
    t.pendown()

def olimpíadas(t):
    # define direção da tartaruga e tamanho da caneta
    t.pensize(3)

    # Cores dos anéis olímpicos
    cores = ['blue', 'black', 'red', 'yellow', 'green']

    # Posições iniciais dos anéis olímpicos
    posicoes = [(-110, -25), (0, -25), (110, -25), (-55, -75), (55, -75)]
    
    for cor, posicao in zip(cores, posicoes):
        t.color(cor)
        jump(t, *posicao)
        t.circle(50)

# Configuração inicial da tela e da tartaruga
s = turtle.Screen()
t = turtle.Turtle()

olimpíadas(t)

# Mantém a janela aberta até que seja fechada manualmente
turtle.done()