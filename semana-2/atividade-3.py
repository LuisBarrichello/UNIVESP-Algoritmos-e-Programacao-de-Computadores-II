A implementação completa da classe Vetor é:

class Vetor(Ponto):
    'uma classe de vetor 2D'
    def __mul__(self, v):
        'produto de vetores'
        return self.x * v.x + self.y * v.y
    def __add__(self, v):
        'adição de vetores'
        return Vector(self.x+v.x, self.y+v.y)
    def __repr__(self):
        'retorna representação de string canônica'
        return 'Vetor{}'.format(self.get())