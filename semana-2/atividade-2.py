""" As implementações aparecem a seguir. O operador == decide que dois baralhos são iguais se tiverem as mesmas cartas e na mesma ordem. """

class Baralho:
    # outros métodos de Baralho
    def __len__(self):
        'retorna tamanho do baralho' return len(self.baralho)
    def __repr__(self):
        'retorna representação de string canônica'
        return 'Baralho ({})'.format(self.baralho)
    def __eq__(self, outro):
        '''retorna True se baralho tiver as
        mesmas cartas na mesma ordem '''
        return self.baralho == outro.baralho