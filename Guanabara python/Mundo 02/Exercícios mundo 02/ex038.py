from datetime import date

atual = date.today().year
nascimento = int( input('Digite o seu ano de nascimento: '))
idade = atual - nascimento

print('Você nasceu em {}, tem {} anos em {}'.format(nascimento, idade, atual))

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Você tem {} anos e terá que se alistar em {} anos'.format(idade, saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você tem {} anos e tinha que ter se alistado a {} anos'.format(idade, saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))