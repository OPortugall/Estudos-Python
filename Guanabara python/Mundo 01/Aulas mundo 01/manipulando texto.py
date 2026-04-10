frase = 'Curso em Vídeo Python' 

print(frase[0:13])
print(frase[9::3])

#Análise
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('android'))
print('Curso' in frase)

#transformação
print(frase.replace('python', 'android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = '   Aprenda Python  '  
print(frase2.strip()) #l ou r, para esquerda ou direita

#divisão
print(frase.split()) #transforma cada palavra em outra separação
print('-'.join(frase)) #adciona algo entre as palavras
print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.''')

