def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(5, 3)
soma(b = 4, a = 5)

def contador(* num):
    for valor in num:
        print(valor, end=' ')
    print('fim')

contador(2, 1, 7)
contador(4, 9, 6)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0]
dobra(valores)
print(valores)

def s(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somandos os valores {valores} temos {s}')

s(2, 3, 6, 8)




