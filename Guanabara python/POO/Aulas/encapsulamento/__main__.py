from classes import ContaBancaria
from rich import inspect

def main():
    c1 = ContaBancaria(111, 'Maria', 5_000)
    c1.depositar(-500)
    c1.sacar(-100)
    c1.saldo = 0
    print(c1)
    inspect(c1, private = True)

if __name__ == '__main__':
    main()