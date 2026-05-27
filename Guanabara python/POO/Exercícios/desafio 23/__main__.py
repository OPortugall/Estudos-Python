from poligono import Quadrado, Circulo
from rich import print 

def main():
    q1 = Quadrado(12)

    print(f'Perimetro do Quadrado = {q1.perimetro():.1f}')
    print(f'Área do Quadrado = {q1.area():.1f}')

    c1 = Circulo (20)
    
    print(f'Perimetro do Circulo = {c1.perimetro():.1f}')
    print(f'Área do Circulo = {c1.area():.1f}')



if __name__ == '__main__':
    main()