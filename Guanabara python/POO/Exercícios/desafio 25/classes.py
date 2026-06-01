from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel 

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass
    
    def painel(self, conteudo):
        frete = Panel(conteudo, title = '[blue] --- Calculando Frete --- [/]', width = 50)
        return frete 

    def proibido(self, proibido):
        proibicao = Panel(proibido, title = '[red] --- Erro na distância --- [/]', width = 55)
        return proibicao
    
    
class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)
        
    
    def calc_frete(self):
        self.frete = self.distancia * self.fator
        conteudo = f'Frete de Moto em {self.distancia}Km = [green]R${self.frete:.2f}[/]'
        return self.painel(conteudo)
        

class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)
       
    
    def calc_frete(self): 
        self.frete = self.distancia * self.fator
        if self.distancia < 50:
            proibido = (f':prohibited: Frete de Caminhão em {self.distancia}Km = Raio mínimo de 50Km')
            return self.proibido(proibido)
        else:
            conteudo = (f'Frete de Caminhão em {self.distancia}Km = [green]R${self.frete:.2f}[/]')
            return self.painel(conteudo)

class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)
        
    
    def calc_frete(self):
        self.frete = self.distancia * self.fator
        if self.distancia > 10:
            proibido = (f':prohibited: Frete de Drone em {self.distancia}Km = Raio máximo de 10Km')
            return self.proibido(proibido)
        else:
            conteudo = (f'Frete de Drone em {self.distancia}Km = [green]R${self.frete:.2f}[/]')
            return self.painel(conteudo)