from math import sqrt 

n = int( input('Digite um número:'))

d = n * 2
t = n * 3
r = sqrt(n)

print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raíz quadada de {} é {:.2f}. \n---FIM---'.format(n, d, n, t, n, r))