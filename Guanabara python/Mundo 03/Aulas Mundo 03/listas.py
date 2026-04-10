num = [2, 5, 4, 3]
print(num)

num[2] = 3
print(num)

num.append(7)
num.sort()
print(num)

num.sort(reverse=True)
print(num)

print(f'Essa lista tem {len(num)} elementos')

num.insert(2, 0)
print(num)

num.pop()
print(num)

if 1 in num:
    num.remove(1)
else:
    print('Não achei o número 1')

valores = []
valores.append(5)
valores.append(4)
valores.append(9)

for pos, v in enumerate(valores):
    print(f'Na posição {pos} eu encontrei o valor {v}')

n = list()

for cont in range(0, 5):
    n.append(int (input('Digite um valor: ')))

for pos, v in enumerate(n):
    print(f'Na posição {pos} eu encontrei o valor {v}')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
