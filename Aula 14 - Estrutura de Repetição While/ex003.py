from time import sleep
print('Entre com dois valores numéricos')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('-' * 20)
menu = 0
while menu != 5:
    menu = int(input('O que deseja fazer?\n'
                   '[1] Somar\n'
                   '[2] Multiplicar\n'
                   '[3] Maior\n'
                   '[4] Novos valores\n'
                   '[5] Sair do programa\n'))
    if menu == 1:
        r = n1 + n2
        print(f'A soma entre {n1} + {n2} é {r}')
        print('-' * 20)
    elif menu == 2:
        r = n1 * n2
        print('O resultado da multiplicação\n'
              f'entre {n1} x {n2} é {r}')
        print('-' * 20)
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
        print('-' * 20)
    elif menu == 4:
        print('Informe os novos valores desejados:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('-' * 20)
    elif menu == 5:
        sleep(1)
        print('Até logo!')
print('Fim do programa...')
