""" 
Problema Prático 4.9

Implemente a função meuGrep(), que toma como entrada duas strings, um nome de arquivo e uma string alvo, e exibe cada linha do arquivo que contém a string alvo como uma substring.

>>> meuGrep('example.txt', 'line')

The 3 lines in this file end with the new line character.

There is a blank line above this line. """

def meuGrep(nomeArquivo, stringAlvo):
    arquivoEntrada = open(nomeArquivo)
    for linha in arquivoEntrada:
        if stringAlvo in linha:
            print(linha, end="")

meuGrep('example.txt', 'lorem')