for c in range(1, 6):
    print('oi')
print('FIM')

print('-=-' * 20)

for c in range(1,6):
    print(c)

print('-=-' * 20)

for c in range(6, 0, -1):
    print(c)

print('-=-' * 20)

for c in range(0, 7, 2):
    print(c)

print('-=-' * 20)

i = int( input('Digite o início: '))
f = int( input('Digite o fim: '))
p = int( input('Digite o passo:'))

for c in range(i, f+1, p):
    print(c)