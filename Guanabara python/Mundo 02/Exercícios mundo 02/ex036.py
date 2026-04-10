from time import sleep

cores = {'limpa' : '\033[m',
         'amarelo' : '\033[1;33m',
         'vermelho' : '\033[1;31m',
         'verde' : '\033[1;32m'}

SeparaStr = str( cores['amarelo'] + '-=-' * 20)
FimSeparaStr = str('-=-' * 20 + cores['limpa'])

print(SeparaStr)
print('Analisador de empréstimo')
print(FimSeparaStr)
sleep(2)

ValorCasa = float( input('Digite o valor da casa: '))
Salario = float( input('Digite o valor do seu salário: R$'))
Anos = int( input('Em quantos anos você vai pagar a casa? '))

Prestacao = (ValorCasa / (Anos * 12))
Excesso = (Salario * 0.3)

sleep(2)

if Prestacao >= Excesso:
    print(cores['vermelho'] + 'Negado! Você não pode pegar o empréstimo pois a prestação é de R${:.2f}!'.format(Prestacao) + cores['limpa'])
else:
    print(cores['verde'] + 'Parabéns!! Seu empréstimo foi aprovado' + cores['limpa'])