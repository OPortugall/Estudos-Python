from rich import print
from rich.panel import Panel 

class Etiqueta:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco 

    def etiqueta(self):
        conteudo = f'{self.nome.center(30, ' ')}'
        conteudo += f'{'-' * 30}'
        precof = f'R${self.preco:,.2f}'
        conteudo += f'{precof.center(30, '-')}'
        etiqueta = Panel(conteudo, title = 'Produto', width = 34)
        print(etiqueta)

c1 = Etiqueta('Iphone 17 pro max', 25_000.85)
c1.etiqueta()
    