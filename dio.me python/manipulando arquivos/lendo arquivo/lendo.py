arquivo = open(r'C:\Users\leolp\OneDrive\Desktop\python\dio.me python\manipulando arquivos\lendo arquivo\lorem.txt', 'r')
print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

for linha in arquivo.readlines():
    print(linha)

#dica
# while len(linha := arquivo.readline()):
  
  # print(linha)
arquivo.close()