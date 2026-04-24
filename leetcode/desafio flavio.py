#Programa original

d = {}

def a():
    x = input('Digite algo: ')
    if x in d:
        print('Já existe')
    else:
        y = input('Digite outra coisa: ')
        d[x] = y
        print('Ok')

def b():
    x = input('Digite algo: ')
    y = input('Digite outra coisa: ')
    if x in d:
        if d[x] == y:
            print('Certo')
        else: 
            print('Errado')
    else: 
        print('Errado')

def c():
    for i in d:
        print(i)

def d1():
    while True:
        print('1')
        print('2')
        print('3')
        print('0')
        k = input()
        if k == '1':
            a()
        elif k == '2':
            b()
        elif k == '3':
            c()
        elif k == '0':
            break

d1()