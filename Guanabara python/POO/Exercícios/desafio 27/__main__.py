from classes import *

def main ():
    p1 = Guerreiro('Pikachu', 1000)
    p2 = Mago('Gandalf', '2000')

    p1.atacar(p2, 100)

if __name__ == '__main__':
    main()