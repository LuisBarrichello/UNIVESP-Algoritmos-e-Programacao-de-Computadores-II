""" 
Problema Prático 6.2

Implemente a função rlookup(), que oferece o recurso de pesquisa reversa de uma agenda de telefones. Sua função aceita, como entrada, um dicionário representando uma agenda de telefones. No dicionário, os números de telefone (chaves) são mapeados para indivíduos (valores). Sua função deverá oferecer uma interface de usuário simples, por meio da qual um usuário pode inserir um número de telefone e obter o nome e sobrenome do indivíduo atribuído a esse número.

>>> agenda_r = {'(123)456-78-90':['Anna','Karenina'],

                '(901)234-56-78':['Yu', 'Tsun'],

                '(321)908-76-54':['Hans', 'Castorp']}

>>> rlookup(agenda_r)

Digite número do telefone no formato (xxx)xxx-xx-xx: (123)456-78-90

('Anna', 'Karenina')

Digite número do telefone no formato (xxx)xxx-xx-xx: (453)454-55-00

O número informado não está em uso.

Digite número do telefone no formato (xxx)xxx-xx-xx:
"""

def rlookup(dicionario):
    continueLoop = True

    while(continueLoop):
        numero = input('Digite número do telefone no formato (xxx)xxx-xx-xx: ')

        if numero in agenda:
            print(agenda[numero])
            continueLoop = False
        else 
            print('O número informado não está em uso.')
            continueLoop = False


agenda_r = {'(123)456-78-90':['Anna','Karenina'],
    '(901)234-56-78':['Yu', 'Tsun'],
    '(321)908-76-54':['Hans', 'Castorp']}

rlookup(agenda_r)