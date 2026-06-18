from senha import *
from rich import print, inspect

def main():
    c = Credencial()
    c.senha = 'olá'
    print(c.validar('Teste'))
    inspect(c, private = True, methods = True)

if __name__ == '__main__':
    main()