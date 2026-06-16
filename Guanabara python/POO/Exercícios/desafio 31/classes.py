from rich import print, inspect

class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = base
        self._altura = altura
        self._area = None

    @property
    def base(self):
        return self._base
    
    @property
    def altura(self):
        return self._altura

    @property
    def area(self):
        return self._base * self._altura
    
    @property
    def medidas(self):
        return (f'Base = {self._base}'
                f'\nAltura = {self._altura}'
                f'\nÁrea = {self.area}')
    