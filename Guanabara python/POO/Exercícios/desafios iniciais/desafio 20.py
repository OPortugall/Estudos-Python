from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key = str.lower)

    def status(self):
        conteudo = f'Nome real: [black on white] {self.nome} [/]'
        conteudo += f'\nJogos Favoritos'
        for num, game in enumerate(self.favoritos):
            conteudo += f'\n:video_game: [blue]{game}[/]'
        painel = Panel(conteudo, title = f'Jogador [red]<{self.nick}>[/]', width = 40)
        print(painel)

j1 = Gamer('Fabricio da Silva', 'Detonator2025')
j1.add_favoritos('Mario Bros.')
j1.add_favoritos('Sonic')
j1.add_favoritos('Fortnite')
j1.status()
