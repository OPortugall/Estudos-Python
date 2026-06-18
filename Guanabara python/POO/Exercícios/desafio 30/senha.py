import hashlib
from rich import inspect, print

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, valor):
        self.__hash = hashlib.sha256(valor.encode('utf-8')).hexdigest()

    def validar(self, chave):
        chave_hash = hashlib.sha256(chave.encode('utf-8')).hexdigest()
        if chave_hash == self.__hash:
            print('Senha Bate!')
            return(chave_hash == self.__hash)
        else:
            print('Senha não bate')
            return(chave_hash == self.__hash)

