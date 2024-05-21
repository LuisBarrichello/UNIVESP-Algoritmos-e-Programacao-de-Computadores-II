""" Problema Prático 6.1

Escreva uma função estadoNasc() que aceite como entrada o nome completo de um presidente dos Estados Unidos (como uma string) e retorne o estado em que ele nasceu. Você deverá usar esse dicionário para armazenar o estado em que cada presidente recente nasceu:

{'Barack Hussein Obama II':'Hawaii',

 'George Walker Bush':'Connecticut',

 'William Jefferson Clinton':'Arkansas',

 'George Herbert Walker Bush':'Massachussetts',

 'Ronald Wilson Reagan':'Illinois',

 'James Earl Carter, Jr':'Georgia'}

>>> estadoNasc('Ronald Wilson Reagan')

'Illinois' """


def estadoNasc(presidente):
    presidentes_nascimento = {
        'Barack Hussein Obama II': 'Hawaii',
        'George Walker Bush': 'Connecticut',
        'William Jefferson Clinton': 'Arkansas',
        'George Herbert Walker Bush': 'Massachussetts',
        'Ronald Wilson Reagan': 'Illinois',
        'James Earl Carter, Jr': 'Georgia'
    }
    
    return presidentes_nascimento.get(presidente, None)

print(estadoNasc('Ronald Wilson Reagan')) # Deve retornar 'Illinois'
