from classes import *
from rich import print, inspect

def main():
    t = Termostato()
    t.temperatura = 17.5
    print(f"A temperatura é de {t.ftemperatura}")

    inspect(t, private = True, methods = True)

if __name__ == "__main__":
    main()