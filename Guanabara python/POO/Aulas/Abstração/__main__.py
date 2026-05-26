from rich import print, inspect
from classes import Pessoa, Aluno, Professor, Funcionario

def main():
    a1 = Aluno('José', 17, 'Informática', 'T01')
    inspect(a1)
    a1.fazer_matricula()
    a1.estudar()

    p1 = Professor('Samuel', 38, 'Biologia', 'Mestrado')
    p1.fazer_aniversario()
    inspect(p1)
    p1.dar_aula()
    p1.estudar()

    f1 = Funcionario('Maria', 25, 'Inspetora', 'Segurança')
    inspect(f1)
    f1.bater_ponto()
    f1.estudar()

if __name__ == '__main__':
    main()