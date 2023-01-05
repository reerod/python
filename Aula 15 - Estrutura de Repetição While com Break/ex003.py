#PAR OU IMPAR
tot_vitoria = 0
import random
comp = random.randint(0, 10)
while True:
    num = int(input('Escolha um inteiro para jogar: '))
    op = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).upper().strip()
    resultado = num + comp
    if op == 'P':
        if resultado % 2 == 0:
            print('VENCEU')
            tot_vitoria += 1
        else:
            print('PERDEU')
            break
    if op == 'I':
        if resultado % 2 == 1:
            print('VENCEU')
            tot_vitoria += 1
        else:
            print('PERDEU')
            break
print(f'Total de vitórias: {tot_vitoria}')
print('Fim de Jogo!')