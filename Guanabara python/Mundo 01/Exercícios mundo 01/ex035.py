cores = {'limpa' : '\033[m',
         'amarelo' : '\033[1;33m',
         'vermelho' : '\033[1;31m',
         'verde' : '\033[1;32m'}

SeparaStr = str(cores['amarelo'] + '-=-' * 20)
FimSeparaStr = str('-=-' * 20 + cores['limpa'])

print(SeparaStr)
print('Analisador de triângulos')
print(FimSeparaStr)

r1 = float( input('Primeiro segmento: '))
r2 = float( input('Segundo segmento: '))
r3 = float( input('Terceiro segmento: '))

condicao = (r1 < r2 + r3 
            and r2 < r1 + r3 
            and r3 < r2 + r1)

if condicao:
    print('{}Os segmentos acima PODEM formar triângulos!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Os segmentos acima NÃO PODEM formar triângulos!{}'.format(cores['vermelho'], cores['limpa']))