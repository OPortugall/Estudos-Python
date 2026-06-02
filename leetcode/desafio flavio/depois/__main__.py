from classes import *
from rich import print
from rich.panel import Panel

def main():

    line = '-=-' * 20

    def title(txt):
        print(line)
        print(txt.center(len(line)))
        print(line)

    def menu(options):
        title('Menu')
        for i, option in enumerate(options, 1):
            print(f'{i} - {option}')

        while True:
            try:
                choose = int(input('Digite uma opção: '))
                if 1 <= choose <= len(options):
                    return choose
                else:
                    print('[red]Opção inválida[/]')
            except:
                print('[red]Digite uma opção válida[/]')

    options = [
        'Criar conta',
        'Realizar login',
        'Usuários',
        'Sair']

    db = BancoDeDados()

    while True:
        response = menu(options)
        match response:
            case 1:
                print(db.CriarConta())
            case 2:
                print(db.Login())
            case 3:
                db.VerificarUsuarios()
            case 4:
                break
        print('\n' * 5)

if __name__ == '__main__':
    main()