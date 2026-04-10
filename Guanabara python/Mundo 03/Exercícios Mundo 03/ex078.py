valores = list()
maior = 0
menor = 0

for cont in range(0, 5):
    valores.append(int (input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print('-=-' * 30)
print(f'Você digitou os valores {valores}!')

print(f'O maior valor digitado foi {maior} na posição ', end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos}... ', end='')
print()

print(f'O menor valor digitado foi {menor} na posição ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos}... ', end='')
print()

