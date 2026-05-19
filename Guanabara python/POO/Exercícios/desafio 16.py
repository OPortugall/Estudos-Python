from rich import print 

class Funcionario:
    #atributos de classe 
    empresa = 'Curso em Vídeo'

    def __init__(self, nome = '', setor = '', cargo = ''):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentação(self) -> str:
        return f':handshake: Olá! Sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}'# ou self.__clas__.empresa
    
c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentação())

c2 = Funcionario('João', 'TI', 'Programador')
print(c2.apresentação())