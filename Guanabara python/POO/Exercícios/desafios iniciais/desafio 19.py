from rich import print 

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f':open_book: Você acabou de abrir o livro [red]{self.titulo}[/] que tem [blue]{self.total_paginas}[/] páginas no total\n Você agora esta na página [green]{self.pagina_atual}[/].')
    
    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False
    
    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f'Pág{self.pagina_atual} -> ', end = '')
                cont += 1
        print(f'Você avançou {cont} páginas e agora esta na página [green]{self.pagina_atual}[/].')
        if self.fim_do_livro():
            print(f':closed_book: [red]Você chegou ao fim do livro {self.titulo}[/]')

    

l1 = Livro('Coisas que aprendi', 85)
l1.avancar_paginas(84)