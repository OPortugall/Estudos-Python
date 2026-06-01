from abc import ABC, abstractmethod
import random
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida 
        self.golpes = []

    def atacar(self, alvo, forca = 50):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'[blue]{self.nome}[/][magenta]({self.vida})[/] atacou [red]{alvo.nome}[/][magenta]({alvo.vida})[/] com um [yellow]{golpe}[/] de força [green]{forca}[/]!')
            alvo.defender(forca)
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer')

    def defender(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator

        if self.vida < 0:
            self.vida = 0
        print(f'[blue]{self.nome}[/] recebeu dano de [red]{fator}[/]!')

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Golpe do Machado', 'Pulo Giratório']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e recuperou [green]{fator}[/] pontos de vida.')

class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Raio de Luz', 'Magia Estática']

    def curar(self):
        fator = random.randint(0, 300)
        self.vida += fator
        print(f'[blue]{self.nome}[/] fez uma magia de cura e recuperou [green]{fator}[/] pontos de vida.')

