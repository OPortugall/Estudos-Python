from rich import print

class Termostato:
    def __init__(self, temperatura = 24):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if 16 <= valor <= 30 and valor % 0.5 == 0:
            self.__temperatura = valor
        elif valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            raise ValueError(f"Temperatura de {valor}°C é inválida!")
    
    @property
    def ftemperatura(self):
        return (f'{self.__temperatura}°C')
        
