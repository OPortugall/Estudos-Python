#decorador sem argumentos

def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar')
        funcao()
        print('Faz algo depois de executar')
    
    return envelope

@meu_decorador
def ola_mundo():
    print(f'Olá mundo!')

ola_mundo()