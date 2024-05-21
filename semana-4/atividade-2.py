



from collections import deque

class Banco:
    def __init__(self):
        self.fila_prioritaria = deque()
        self.fila_normal = deque()

    def inserir_pessoa(self, idade):
        if idade > 60:
            self.fila_prioritaria.append(idade)
        else:
            self.fila_normal.append(idade)

    def sair_pessoa(self):
        # Primeiro, sai uma pessoa da fila prioritária
        if self.fila_prioritaria:
            self.fila_prioritaria.popleft()
        # Depois, sai uma pessoa da fila normal
        if self.fila_normal:
            self.fila_normal.popleft()

    def processar_filas(self):
        while self.fila_prioritaria or self.fila_normal:
            self.sair_pessoa()

# Exemplo de uso
banco = Banco()

# Inserindo pessoas na fila
banco.inserir_pessoa(55) # Idade 55, entra na fila normal
banco.inserir_pessoa(65) # Idade 65, entra na fila prioritária
banco.inserir_pessoa(70) # Idade 70, entra na fila prioritária
banco.inserir_pessoa(45) # Idade 45, entra na fila normal

# Processando as filas
banco.processar_filas()

print(banco.fila_normal)
print(banco.fila_prioritaria)
