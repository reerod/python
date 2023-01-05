#TABUADA v3.0
tab = int(input('Qual número deseja saber a tabuada? '))
while True:
    print('-' * 40)
    if tab < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{tab} X {c} = {tab*c}')
        print('-' * 40)
        tab = int(input('Qual número deseja saber a tabuada? '))
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
