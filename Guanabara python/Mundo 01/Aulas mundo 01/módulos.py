'''
import math:
ceil
floor
trunc
pow
sqrt
factorial
from math import sqrt
somente sqrt
'''
#import math
from math import sqrt, hypot

num = int( input('Digite um número:'))
#r = math.sqrt (num)
r = sqrt (num)

print(r)

co = int( input('Cateto oposto:'))
ca = int( input('Cateto Adjascente:'))
#hi = math.sqrt (co ** 2 + ca ** 2)
hi = hypot (co, ca)

print('A hipotenusa deste triângulo é: {}'.format(hi))