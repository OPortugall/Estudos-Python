from abc import ABC, abstractmethod
from rich import print

contas = {}

class BancoDeDados():
    def __init__(self, nome = 'Banco de Dados', tipo = 'Contas'):
        self.nome = nome
        self.tipo = tipo
        
    def CriarConta(self):
        self.nome_usuario = input('Nome de usuário: ')
        if self.nome_usuario in contas:
            return('[red]Esse nome de usuário já existe![/]')
        else:
            self.senha = input('Digite sua senha: ')
            contas[self.nome_usuario] = self.senha
            return('[green]Certo! Conta criada![/]')

    def Login(self):
        self.nome_usuario = input('Nome de usuário: ')
        self.senha = input('Senha: ')
        if self.nome_usuario in contas:
            try: 
                if contas [self.nome_usuario] == self.senha:
                    return ('[green]Login realizado com sucesso![/]')
            except:
                return('[red]Dados inválidos! Tente novamente![/]')
        else: 
            return('[red]Dados inválidos! Tente novamente![/]')

    def VerificarUsuarios(self):
        for i in contas:
            print(i)

