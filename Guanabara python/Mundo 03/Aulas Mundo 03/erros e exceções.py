n = int( input('Numerador: '))
d = int( input('Denominador: '))

try: 
    r = n / d
except Exception as erro:
    print(f'Infelizmente tivemos um problema. O erro foi {erro.__class__}')
else:   
    print(f'A divisão é {r}')
finally:
    print('Volte sempre!')