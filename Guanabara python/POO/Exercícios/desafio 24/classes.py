from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    
    def Preparar(self):
        print('--- Iniciando o Preparo ---')
        self.Ferver_Agua()
        self.Misturar()
        self.servir()
        print('--- Bebida Pronta ---\n')

    def Ferver_Agua(self):
        print('1. Fervendo água a 100 graus Celsius.')

    @abstractmethod
    def Misturar(self):
        pass

    @abstractmethod
    def servir(self):
         pass


class Cafe(BebidaQuente):
    def Misturar(self):
        print('2. Passando água pressurizada pelo pó de café moído.')

    def servir(self):
        print('3. Servindo em xícara pequena.')


class Cha(BebidaQuente):
    def Misturar(self):
        print('2. Mergulhando o sachê de ervas na água.')

    def servir(self):
        print('3. Servindo na caneca de porcelana com limão')


class Leite(BebidaQuente):
    def Misturar(self):
        print('2. Passando vapor pressurizado pelo bico do leite.')

    def servir(self):
        print('3. Servindo na caneca grande já com café.')