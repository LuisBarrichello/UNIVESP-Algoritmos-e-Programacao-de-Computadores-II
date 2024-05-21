""" 
Problema Prático 6.4

Implemente a função contaPalavra(), que aceite como entrada um texto — como uma string — e exiba a frequência de cada palavra no texto. Você pode considerar que o texto não possui pontuação e que as palavras são separadas por espaços em branco.

>>> texto = 'all animals are equal but some \

animals are more equal than others'

>>> contaPalavra(texto)

all      appears 1 time.

animals  appears 2 times.

some     appears 1 time.

equal    appears 2 times.

but      appears 1 time.

are      appears 2 times.

others   appears 1 time.

than     appears 1 time.

more     appears 1 time.
"""

def contaPalavra(texto):
    listaDePalavras = texto.split()
    contadores = { }

    for palavra in listaDePalavras:
        if palavra in contadores:
            contadores[palavra] += 1
        else:
            contadores[palavra] = 1
    
    for palavra in contadores:
        if contadores[palavra] == 1:
             print('{:8} aparece {} vez.'.format(palavra, contadores[palavra]))
        else:
            print('{:8} aparece {} vezes.'.format(palavra, contadores[palavra]))

texto = 'all animals are equal but some animals are more equal than others'
contaPalavra(texto)