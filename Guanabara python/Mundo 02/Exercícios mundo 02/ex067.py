linha = ('-' * 20)
c = 1

while True :
    n = int( input('De qual número você quer ver a tabuada? '))
    if n < 0:
        break
    print(linha)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
        c += 1
    print(linha)
print('FIM')