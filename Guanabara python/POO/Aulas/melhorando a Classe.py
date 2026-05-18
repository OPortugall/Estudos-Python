#Declaração de Classe

class Gafanhoto:
    def __init__(self, nome = "Vazio", idade = 0): #Método Construtor
        #atributos de instância
        self.nome = nome
        self.idade = idade

    #Métodos de instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade. "
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
    
#Declaração de Objeto
g1 = Gafanhoto(nome = "João", idade = 17)
g1.aniversario()
print(g1)

g2 = Gafanhoto("Maria", 53)
print(g2)
print(g2.__dict__)
print(g2.__getstate__())