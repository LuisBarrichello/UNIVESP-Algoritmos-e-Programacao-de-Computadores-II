""" Problema Prático 4.8
Escreva a função palavras() que aceita um argumento de entrada — um nome de arquivo — e retorna a lista de palavras reais (sem símbolos de pontuação !,.:;?) no arquivo.

>>> palavras('example.txt')

['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with',

 'the', 'new', 'line', 'character', 'There', 'is', 'a',

 'blank', 'line', 'above', 'this', 'line'] """


def palavras(nameFile):
    pontuacoes = "!,.:;?"
    listWords = []

    with open(nameFile, 'r') as arquivo:
        for linha in arquivo:
            # Remove os símbolos de pontuação da linha
            for pontuacao in pontuacoes:
                linha = linha.replace(pontuacao, '')

                # Adiciona as palavras da linha à lista, excluindo as strings vazias
                listWords.extend(word for word in linha.split() if word)

    return listWords


print(palavras('example.txt'))
