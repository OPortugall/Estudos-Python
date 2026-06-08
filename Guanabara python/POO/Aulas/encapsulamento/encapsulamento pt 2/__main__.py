from classe import *
from rich import inspect

def main():
    av1 = Avaliacao('Pedro', 'Matematica')
    av1.set_nota(7.3)
    inspect(av1, private = True)
    print(f'{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}')

if __name__ == '__main__':
    main()