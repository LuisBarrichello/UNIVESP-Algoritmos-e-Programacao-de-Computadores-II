""" Quando criado, um objeto Retângulo não tem variáveis de instância. O método setTamanho() deverá criar e inicializar variáveis de instância para armazenar a largura e o comprimento do retângulo. Essas variáveis de instância são então usadas pelos métodos perímetro() e área(). Em seguida, está a implementação da classe Retângulo. """

class Retângulo:
    'classe que representa retângulos'

    def setTamanho(self, coordx, coordy):
        'construtor '
        self.x = coordx
        self.y = coordy

    def perímetro(self):
        'retorna perímetro do retângulo'
        return 2*(self.x+self.y)
        
    def área(self):
        'retorna área do retângulo'
        return self.x*self.y