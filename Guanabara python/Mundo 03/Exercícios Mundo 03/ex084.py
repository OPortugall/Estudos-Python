dados = list()
pessoa = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        maior = menor = dados[1]
    else:
        if dados [1] > maior:
            maior = dados[1]
        if dados [1] < menor:
            menor = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar? [S/N]'))
    while opcao not in 'SsNn':
        opcao = str( input('Erro! Quer continuar? [S/N]'))
    if opcao in 'Nn':
        break

print('-=-' * 30)
print(f'Ao todo você cadastrou {len(pessoa)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoa:
    if p[1] == maior:
        print(f'{p[0]}... ', end='')

print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoa:
    if p[1] == menor:
        print(f'{p[0]}... ', end='')