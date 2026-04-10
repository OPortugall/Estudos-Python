name = str( input('Digite seu nome completo: ')).strip()

ma = name.upper()
mi = name.lower()
letras = (len(name) - name.count(' '))
separa = name.split()

print(
    'Analisando seu nome...\n' \
    'Seu nome em maiúsculas é: {}\n' \
    'Seu nome em minúsculas é: {}\n' \
    'Seu nome tem ao todo tem {} letras\n' \
    'Seu primeiro nome é {} e ele tem {} letras'.format(ma, mi, letras, separa[0], len(separa[0]))
)

if name == 'Leonardo Lemgruber Portugal':
    print(
        '-----------' \
        'Você é muito lindo, parabéns' \
        '-----------'
        )