#PROGREÇÃO ARITMÉTICA

p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
total = 0
termo = 10
while termo != 0:
    total = total + termo
    while cont <= total:
        print(p1, end=' --> ')
        p1 += razao
        cont = cont + 1
    print('PAUSA')
    termo = int(input('\nQuer mostrar mais quantos termos? '))

print(f'O total de termos foi de {total}.')
