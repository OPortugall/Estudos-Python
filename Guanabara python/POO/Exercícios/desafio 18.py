from rich.panel import Panel
from rich import print 

class Churrasco:
    """

    Outro jeito de fazer o calculo:

    consumo_padrao = 0.400
    preco_kg = 82.40

    def calcular_qtd_carne(self):
        return self.quant * Churrasco.consumo.padrao
    def calcular_custo_total(self):
        return self.calcular_qtd_carne() * self.__clas__.preco_kg

    def calcular_custo_individual(self):
        return calcular_custo_total() / self.quant

    ficaria: conteudo += f'Recomendo comprar {self.calcular_qtd_carne():.2f}kg de carne'
    """


    def __init__(self, titulo, quantidade):
        self.titulo = titulo 
        self.quant = quantidade 

    def calculo(self):
        carne = self.quant * 0.4
        total = carne * 82.40
        pessoa = total / self.quant 

        return carne, total, pessoa 

    def Painel(self):

        carne, total, pessoa = self.calculo()

        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.quant}[/]\n'
        conteudo += f'Cada participante comerá 0.4Kg e cada Kg custa R$82.40\n'
        conteudo += f'Recomendo comprar [blue]{carne:.2f}[/]KG de carne\n'
        conteudo += f'O custo total será de [green]R${total:,.2f}[/]\n'
        conteudo += f'Cada pessoa pagará [yellow]R${pessoa:,.2f}[/]'

        calcular = Panel(conteudo, title = self.titulo, width = 80)

        print(calcular)
    
c1 = Churrasco('Churras dos Amigos', 15)
c1.Painel()