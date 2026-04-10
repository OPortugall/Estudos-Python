pessoa = list()
pessoa.append('Gustavo')
pessoa.append(40)

galera = list()
galera.append(pessoa[:])

pessoa[0] = 'Maria'
pessoa[1] = 22
galera.append(pessoa[:])

print(galera)

grupo = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Lucena', 45]]
print(grupo[2][1])
print(grupo)
print(grupo[1])

pessoal = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoal.append(dado[:])
    dado.clear()
print(pessoal)