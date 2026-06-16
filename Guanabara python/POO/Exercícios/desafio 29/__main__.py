from classes import *
from rich import inspect


def main():
    d = Diario('Gafanhoto')

    d.escrever('Primeira mensagem')
    d.escrever('Você é uma pessoa simpática')
    d.escrever('Você gosta de python')

    d.ler('Gafanhoto')
    d.senha = 'Oi'
    inspect(d, private = True, methods = True)

if __name__ == "__main__":
    main()