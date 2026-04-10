valor = list()

while True:
    valor.append(int (input('Digite um valor: ')))
    print('Valor adcionado com sucesso...')
    opcao = str(input('Você quer continuar? [S/N] '))
    while opcao not in 'SsNn':
        opcao = str(input('Erro! você quer continuar? [S/N] '))
    if opcao in 'Nn':
        break
valor.sort()
print(f'Os valores digitados foram {valor}')
