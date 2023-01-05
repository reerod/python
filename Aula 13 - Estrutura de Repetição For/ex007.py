'''EX007 - Números Primos'''
cont = 0
num = int(input('Digite um numero: '))
for c in range(1, num+1):
    print(c, end=' ')
    if num % c == 0:
        cont += 1
print(f'\nO número {num} foi divisível {cont} vezes.')
if cont == 2:
    print('Ele é primo.')
else:
    print('Não é primo.')