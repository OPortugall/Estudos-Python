num = int( input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão\n' \
'[1] converter para Binário\n' \
'[2] converter para Octal\n' \
'[3] converter para Hexadecimal')

opcao = int( input('Digite sua opção: '))

if opcao == 1:
    print('{} convertido para binário é igual a: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')