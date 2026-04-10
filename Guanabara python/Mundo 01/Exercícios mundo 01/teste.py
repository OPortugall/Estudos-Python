def cor(texto, nome_cor):
    cores = {
        'limpa': '\033[m',
        'amarelo': '\033[1;33m',
        'vermelho': '\033[1;31m',
        'verde': '\033[1;32m',
        'azul': '\033[1;34m',
        'roxo': '\033[1;35m',
        'ciano': '\033[1;36m'
    }
    return cores.get(nome_cor, cores['limpa']) + texto + cores['limpa']


def linha(tam=40):
    return '-' * tam


def titulo(txt):
    print(cor(linha(), 'amarelo'))
    print(cor(txt.center(40), 'azul'))
    print(cor(linha(), 'amarelo'))


def menu(opcoes):
    titulo('MENU PRINCIPAL')
    for i, opcao in enumerate(opcoes, 1):
        print(cor(f'{i} - {opcao}', 'ciano'))
    print(cor(linha(), 'amarelo'))

    while True:
        try:
            escolha = int(input(cor('Escolha uma opção: ', 'verde')))
            if 1 <= escolha <= len(opcoes):
                return escolha
            else:
                print(cor('Opção inválida!', 'vermelho'))
        except:
            print(cor('Digite um número válido!', 'vermelho'))

opcoes = ['Analisar triângulo', 'Sair']

while True:
    resposta = menu(opcoes)

    if resposta == 1:
        titulo('Analisador de Triângulos')

        r1 = float(input('Primeiro segmento: '))
        r2 = float(input('Segundo segmento: '))
        r3 = float(input('Terceiro segmento: '))

        if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
            print(cor('PODE formar um triângulo!', 'verde'))
        else:
            print(cor('NÃO PODE formar um triângulo!', 'vermelho'))
            
    elif resposta == 2:
        titulo('Saindo do sistema...')
        break