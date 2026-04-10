from time import sleep

cores = {'limpa' : '\033[m',
         'amarelo' : '\033[1;33m',
         'vermelho' : '\033[1;31m',
         'verde' : '\033[1;32m'}

linha = (cores['amarelo'] + '-=-' * 20 + cores['limpa'])

Valor1 = int( input('Primeiro valor: '))
Valor2 = int( input('Segundo valor: ')) 
opcao = 0

while opcao != 5:
    print(linha + cores['amarelo'] + '\n[1] somar\n' \
    '[2] multiplicar\n' \
    '[3] maior\n' \
    '[4] novos números\n' \
    '[5] sair do programa\n' + cores['limpa'] + linha)
    opcao = int( input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = Valor1 + Valor2
        print(cores['verde'] + '{} + {} = {}'.format(Valor1, Valor2, soma) + cores['limpa'])
    elif opcao == 2:
        multiplicacao = Valor1 * Valor2
        print(cores['verde'] + '{} x {} = {}'.format(Valor1, Valor2, multiplicacao) + cores['limpa'])
    elif opcao == 3:
        if Valor1 > Valor2:
            maior = Valor1
        else:
            maior = Valor2
        print(cores['verde'] + 'Entre {} e {} o maior valor é {}'.format(Valor1, Valor2, maior) + cores['limpa'])
    elif opcao == 4:
        print('Informe os números novamente: ')
        Valor1 = int( input('Primeiro valor: '))
        Valor2 = int( input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print(cores['vermelho'] + 'Opção inválida. Tente Novamente' + cores['limpa'])
print(linha + cores['amarelo'] + '\nFim do programa\n' + linha)