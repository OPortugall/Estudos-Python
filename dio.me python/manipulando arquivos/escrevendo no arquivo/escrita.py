arquivo = open(r'C:\Users\leolp\OneDrive\Desktop\python\dio.me python\manipulando arquivos\escrevendo no arquivo\teste.txt', 'w')

arquivo.write('Escrevendo dados em um novo arquivo.')
arquivo.writelines(['\n', 'escrevendo ', '\n', 'um ', '\n', 'novo ', '\n', 'texto'])
arquivo.close()