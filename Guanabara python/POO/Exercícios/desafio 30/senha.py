import hashlib
from rich import inspect

class Credencial:
    def __init__(self, senha):
        self.__senha = None
        self.senha = senha

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, valor):
        texto_bytes = valor.encode('utf-8')
        hash_gerado = hashlib.sha256(texto_bytes)
        self.__senha = hash_gerado.hexdigest()

d = Credencial
d.senha = 'ABC'
inspect(d, private = True, methods = True)
