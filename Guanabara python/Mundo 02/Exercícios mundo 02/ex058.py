from random import randint

computador = randint(0, 10)

cores = {'limpa' : '\033[m',
         'amarelo' : '\033[1;33m',
         'vermelho' : '\033[1;31m',
         'verde' : '\033[1;32m'}

SeparaStr = (cores['amarelo'] + '-=-' * 20)
FimSeparaStr = ('-=-' * 20 + cores['limpa'])

print(SeparaStr)
print('Eu estou pensando em um número entre 0 e 10.\n' \
'Será que você consegue advinhar?')
print(FimSeparaStr)

acertou = False
tentativa = 0

while not acertou:
    jogador = int( input('Digite o número que estou pensando: '))
    tentativa = tentativa + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(cores['vermelho'] + 'Mais... Tente outra vez: ' + cores['limpa'])
        elif jogador > computador:
            print(cores['vermelho'] + 'Menos... Tente outra vez: ' + cores['limpa'])
print(cores['verde'] + 'Acertou com {} tentativas. Parabéns'.format(tentativa) + cores['limpa'])
    
