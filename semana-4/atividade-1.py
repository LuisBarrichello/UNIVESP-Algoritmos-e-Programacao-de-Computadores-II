""" Implementar um programa em Python que
realiza a conversão decimal para binário
usando pilha """

from Pilha import Pilha

def conversorParaBinario(valor):
    pilha = Pilha()

    while(valor > 0): 
        resto = valor % 2
        valor = valor // 2

        pilha.push(resto)
    
    binary_representation = ""

    while not pilha.empty():
        binary_representation += str(pilha.pop())

    return binary_representation


binary_number = conversorParaBinario(13)
print(binary_number)