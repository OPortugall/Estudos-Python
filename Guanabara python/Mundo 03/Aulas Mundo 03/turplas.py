lanche = ('hamburguer', 'pizza', 'suco', 'pudim')
print(lanche)
print(lanche[2])
print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posíção {pos}')

print(sorted(lanche))