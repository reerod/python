'''EX008 - Leitor de Palíndromos'''
frase = str(input('Escreva uma palavra ou frase: ')).upper().strip()
dividir = frase.split()
juntar = ''.join(dividir)
inverso = ''
for c in range (len(juntar) - 1, -1, -1):
    inverso += juntar[c]
print(juntar, inverso)
if inverso == juntar:
    print('Temos um PALÍNDROMO.')
else:
    print('A frase/palavra informada não forma um palíndromo.')