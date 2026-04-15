"""help(input)
print(input.__doc__)"""

def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}', end = ' - ')
        c += p
    print('FIM!')

contador(2, 10, 2)

def somar(a, b, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 4, 8)
somar(4, 6)

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')

def soma(a = 0, b = 0, c = 0):
    s = a + b + c
    return s

r1 = soma(3, 2, 5)
r2 = soma(1, 7)
r3 = soma(4, 8)

print(f'Os resultados foram {r1}, {r2} e {r3}')