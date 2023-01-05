'''EX005 - Soma dos Pares'''
total = 0
soma = 0
for i in range (1, 7):
    num = int(input(f'Informe o {i}º valor: '))
    if num % 2 == 0:
        soma += num
        total += 1
print(f'O resultado da soma dos {total} '
    f'valores pares digitados é {soma}.')
