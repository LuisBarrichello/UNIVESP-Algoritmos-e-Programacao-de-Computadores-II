""" 
Problema Prático 10.1

Implemente o método recursivo reverse(), que aceita um inteiro não negativo como entrada e exibe os dígitos de n verticalmente, começando com o dígito de ordem baixa.

>>> reverse(3124)
4
2
1
3
"""

def reverse(numero):
    if numero < 10:
        print(numero)
    else:
        print(numero%10)
        reverse(numero//10)