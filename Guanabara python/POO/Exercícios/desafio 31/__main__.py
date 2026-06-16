from rich import inspect
from classes import *

def main():
    d = Retangulo(4, 5)

    inspect(d, private = True, methods = True)

if __name__ == "__main__":
    main()