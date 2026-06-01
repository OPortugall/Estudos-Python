from classes import * 
from rich import inspect

def main():
    f1 = Horista ('José da Silva', 12, 190)
    f1.calcular_salario()
    f1.analisar_salario()

    f2 = Mensalista ('Maria Souza', 8500)
    f2.calcular_salario()
    f2.analisar_salario()

    
if __name__ == '__main__':
    main()