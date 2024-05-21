class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y

    def get(self):
        return self.x, self.y

    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

ponto = Point(0,0)
ponto.setx(5)
print(ponto)