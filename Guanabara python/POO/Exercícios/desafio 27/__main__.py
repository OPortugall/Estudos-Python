from classes import *

def main ():
    p1 = Guerreiro('Pikachu', 1000)
    p2 = Mago('Gandalf', 10)

    p1.atacar(p2, 1000)
    p2.curar()
    
    p2.atacar(p1, 200)


if __name__ == '__main__':
    main()