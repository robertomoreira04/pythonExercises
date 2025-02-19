class Forma:

    def area():
        pass #serve para criar uma função sem valor

class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado 

    def area(self):
        return self.lado ** 2
    
class Circulo(Forma):
    
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2
    
quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)

circulo = Circulo(4)
area_circulo = circulo.area()
print(area_circulo)
