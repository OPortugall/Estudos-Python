from rich import print 
from rich.panel import Panel
from rich.table import Table
from rich import inspect

print('Olá, [red]Mundo[/]! :earth_americas:')
print('Olá [bold blue]Pequeno Gafanhoto[/]! :vulcan_salute:')

caixa = Panel('[white]Esse aqui é um painel de exemplo[/]:+1:', title = 'Mensagem', style = 'red', width = 40)
print(caixa)

tabela = Table(title = 'Tabela de preços')

tabela.add_column('Nome', justify = 'left', style = 'red')
tabela.add_column('Preço', justify = 'center', style = 'blue')

tabela.add_row('Lápis', 'R$1,50')
tabela.add_row('Borracha', 'R$5,00')

print(tabela)

inspect(int, all = True)