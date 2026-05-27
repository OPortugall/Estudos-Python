from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, comprimento):
        self.comp_lado = comprimento
    
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, comprimento):
        super().__init__(comprimento)
        self.qtd_lados = 4

    def perimetro(self):
        per = self.qtd_lados * self.comp_lado
        return per
    
    def area(self):
        ar = self.comp_lado * self.comp_lado
        return ar
    
class Circulo(Poligono):
    def __init__(self, comprimento):
        super().__init__(comprimento)
        self.raio = self.comp_lado
    
    def perimetro(self):
        per = 2 * pi * self.raio
        return per
    
    def area(self):
        ar = pi * (self.raio ** 2)
        return ar
    