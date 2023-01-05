'''Ex002 - Contagem de Pares'''
contador = 0
num1 = int(input('Inicie com um inteiro: '))
num2 = int(input('Termine com um inteiro: '))
for i in range (num1, num2+1):
    print(i, end='.. ')
    if i % 2 == 0:
        contador += 1
print('\nFim da contagem.')
print(f'Ao todo, tivemos {contador} números pares.')