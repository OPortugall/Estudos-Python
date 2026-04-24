#meu programa

BancoDeDados = {}

line = '-=-' * 20

def title(txt):
    print(line)
    print(txt.center(len(line)))
    print(line)

def CiarConta():
    x = input('Nome de usuário: ')
    if x in BancoDeDados:
        print('Esse nome de usuário já existe!')
    else:
        y = input('Digite sua senha: ')
        BancoDeDados[x] = y
        print('Certo! Conta criada!')

def Login():
    x = input('Nome de usuário: ')
    y = input('Senha: ')
    if x in BancoDeDados:
        try: 
            if BancoDeDados[x] == y:
                print('Login realizao com sucesso!')
        except:
            print('Dados inválidos! Tente novamente!')
    else: 
        print('Dados inválidos! Tente novamente!')

def VerificarUsuarios():
    for i in BancoDeDados:
        print(i)

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
                print('Opção inválida')
        except:
            print('Digite uma opção válida')

options = [
    'Criar conta',
    'Realizar login',
    'Usuários',
    'Sair']

while True:
    response = menu(options)
    match response:
        case 1:
            CiarConta()
        case 2:
            Login()
        case 3:
            VerificarUsuarios()
        case 4:
            break

