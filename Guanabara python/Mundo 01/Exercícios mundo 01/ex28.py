from random import randint
from time import sleep

computador = randint(0, 5)

print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5, você consegue descobrir qual é?')
print('-=-' * 20)
jogador = int( input('Digite o número em que estou pensando: '))

print('PROCESSANDO....')
sleep(2)

if jogador == computador:
    print('Você acertou!😍')
else:
    print('Eu ganhei, pensei no número {} e não no {}!'.format(computador, jogador))