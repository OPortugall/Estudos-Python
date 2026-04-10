print('Gerador de PA')
print('-=-' * 20)

primeiro = int( input('Digite o primeiro termo: '))
razao = int( input('Digite o termo da razão: '))
termo = primeiro
c = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        c = c + 1
    print('PAUSA')
    mais = int( input('Quantos termos a mais você quer mostrar? '))
print('FIM')
print('Sua progressão teve {} termos'.format(total))