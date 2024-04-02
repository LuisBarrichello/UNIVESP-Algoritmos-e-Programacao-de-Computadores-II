""" Problema Prático 3.14

Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista. Você pode considerar que a lista não estará vazia. A função não deverá retornar nada.

>>> ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']

>>> trocaPU(ingredientes)

>>> ingredientes

['maçãs', 'açúcar', 'manteiga', 'farinha'] """

def trocaPU(listItems):
    if len(listItems) != 0:
        temp = listItems[0]
        listItems[0] = listItems[-1]
        listItems[-1] = temp
    print(listItems)
    return listItems

ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
trocaPU(ingredientes)