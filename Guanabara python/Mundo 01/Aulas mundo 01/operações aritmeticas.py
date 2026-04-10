'''
+ adição
- subtração
* multiplicação
/ divisão
** Potência
// Divisão Inteira
% Resto da divisão

'''
n1 = int( input('Digite um valor:'))
n2 = int( input('Digite outro valor:'))

s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2

print('A soma é: {}, a multiplicação é: {} e a divisão é: {:.3f}'.format(s, m, d), end=' ')
print('A potência é: {} \na divisão inteira é: {} \ne o resto é: {}'.format(p, di, r))

v = int( input('Digite o número:'))

print('O antecessor de {} é: {} \nO seu sucessor é: {}'.format(v, v-1, v+1))