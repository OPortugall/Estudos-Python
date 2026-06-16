from rich import print, inspect

class Diario:
    
    def __init__(self, senhamestra = 'Pato'):
        self.__senha = senhamestra
        self.__segredos = []

    @property
    def senha(self):
        raise PermissionError('Ninguém tem permissão de ver a senha')
    
    @senha.setter
    def senha(self, msg):
        raise PermissionError('Ninguém pode alterar a senha!')
    
    def escrever(self, msg):
        self.__segredos.append(msg)
       
    def ler(self, senha = None):
        if senha == self.__senha:
            print('[green]DIARIO LIBERADO![/]')
            for msg in self.__segredos:
                print(f'- {msg}')
        else:
            raise PermissionError('Senha inválida! Você não pode ler meu diário!')


    
    