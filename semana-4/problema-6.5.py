""" 
Problema Prático 6.5

Use a função lookup()para implementar uma aplicação de pesquisa de agenda. Sua função aceita, como entrada, um dicionário representando uma agenda. No dicionário, as tuplas contendo nomes e sobrenomes de indivíduos (as chaves) são mapeadas a strings contendo números de telefone (os valores). Veja aqui um exemplo:

>>> agenda = {('Anna','Karenina'):'(123)456-78-90',

              ('Yu', 'Tsun'):'(901)234-56-78',

              ('Hans', 'Castorp'):'(321)908-76-54'}

Sua função deverá oferecer uma interface simples com o usuário, por meio da qual ele possa informar o nome e sobrenome de um indivíduo e obter o número de telefone atribuído a esse indivíduo.

>>> lookup(agenda)

Digite o nome: Anna

Digite o sobrenome: Karenina

(123)456-78-90

Digite o nome: Yu

Digite o sobrenome: Tsun

(901)234-56-78
"""

def lookup(agenda):
    continuaLoop = True

    while(continuaLoop):
        nome = input('Digite o nome: ')
        sobrenome = input('Digite o sobrenome: ')
        pessoa = (nome, sobrenome)
        if pessoa in agenda:
            print(agenda[pessoa])
        else:
            print('O nome informado não é conhecido.')

agenda = {('Anna','Karenina'):'(123)456-78-90',
    ('Yu', 'Tsun'):'(901)234-56-78',
    ('Hans', 'Castorp'):'(321)908-76-54'}

lookup(agenda)