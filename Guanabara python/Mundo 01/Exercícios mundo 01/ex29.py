carro = float( input('Qual a velocidade atual do caror?'))
multa = (carro - 80) * 7 

if carro <= 80:
    print('Tudo bem, tenha um bom dia!')
else:
    print('MULTADO! Você excedeu o limite permitido de 80Km/H\n' \
    'Você deve pagar uma multa de R$ {:.2f}!\n' \
    'Tenha um bom dia!'.format(multa))

