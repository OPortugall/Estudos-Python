from abc import ABC, abstractmethod
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida 
        self.golpes = []

    def atacar(self, alvo, forca = 50):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'{self.nome} atacou {alvo.nome} com um {golpe}')
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer')

    def defender(self, dano):
        fator = random.randint(0, dano)
        self.vida = self.vida - fator

        if self.vida < 0:
            self.vida = 0
        print(f'{self.nome} recebeu dano de {fator}!')

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Golpe do Machado', 'Pulo Giratório']

    def curar(self):
        pass

class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Raio de Luz', 'Magia Estática']

    def curar(self):
        pass

