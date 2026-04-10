nome = str( input('Digite o seu nome:'))

if nome == 'Leonardo':
    print('Que nome bonito!')
elif nome == 'Octávio':
    print('Você é um irmão muito legal')
elif nome in 'Ana Cláudia Portugal Jorge':
    print('Que belo nome também')
else:
    print('Seu nome é bem normal...')

print('Tenha um bom dia, {}!'.format(nome))