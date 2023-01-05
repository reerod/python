frase = 'Curso em Video Python'
#Fatiamento de Strings
'''print(frase[9])
print(frase[9:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(frase[::])'''
#Análise de Strings
print(f'frase = {frase}')
print('comprimento de uma string (considerando os espaços entre elas)')
print(len(frase))
print('comprimento de uma string (desconsiderando os espaços entre elas)')
print(len(frase) - frase.count(' '))
print('count() conta quantas vezes uma string aparece dentro da frase (sem fatiar)')
print(frase.count('o'))
print('count() contar e fatiar ao mesmo tempo')
print(frase.count('o',0,14))
print('find() procura a posição em que uma string está')
print(frase.find('deo'), frase.find('yt'), frase.find('z'), frase.find(' '))
print('in para descobrirmos se existe ou não uma string na frase')
print('Python' in frase, 'Estudar' in frase)