from rich.panel import Panel
from rich import print 

class Churrasco:
    
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