from classes import *

def main ():
    dist = 90
    m1 = Moto(dist)
    print(m1.calc_frete())

    c1 = Caminhao(dist)
    print(c1.calc_frete())

    d1 = Drone(dist)
    print(d1.calc_frete())


if __name__ == '__main__':
    main()