""" 
Problema Prático 6.6

Implemente a função sync() que aceita uma lista de agendas (em que cada agenda é um conjunto de números de telefone) como entrada e retorna uma agenda (como um conjunto) contendo a união de todas as agendas.

>>> agenda4 = {'234-56-78', '456-78-90'}

>>> agendas = [agenda1, agenda2, agenda3, agenda4]

>>> sync(agendas)

{'234-56-78', '456-78-90', '123-45-67', '345-67-89'}
"""

def sync(agendas):
    'retorna a união de conjuntos em agendas'
    res = set() # inicializa o acumulador

    for agenda in agendas:
        res = res | agenda # acumula agenda em res

    return res


agenda1 = {'123-45-67', '234-56-78', '345-67-89','123-45-67', '345-67-89'}
agenda1 = {'193-45-64', '236-36-18'}
agenda3 = {'345-67-89', '456-78-90'}
agenda4 = {'237-56-78', '496-78-90'}

agendas = [agenda1, agenda2, agenda3, agenda4]

sync(agendas)