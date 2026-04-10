print('Gerador de PA')
print('-=-' * 20)

primeiro = int( input('Digite o primeiro termo: '))
razao = int( input('Digite o termo da razão: '))
termo = primeiro
c = 1

while c <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    c = c + 1
print('fim')