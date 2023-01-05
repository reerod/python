'''EX004 - Tabuada V.2.0'''
print('-='*20)
print('***TABUADA DE MULTIPLICAR***')
tab = int(input('Informe a tabuada que deseja visualizar: '))
for n in range (1, 11):
    res = tab * n
    print(f'{tab} X {n} = {res}')
print('-='*20)