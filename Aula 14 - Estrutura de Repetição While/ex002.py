from random import randint
comp = randint(0, 10)
jogador = 0
tentativas = 0
totjogadas = 0
print('-=' * 26)
print('JOGO DA ADIVINHAÇÃO v2.0'.center(50))
print('-=' * 26)
while jogador != comp:
    jogador = int(input('Em que número eu pensei?\n'))
    totjogadas += 1
    if jogador > comp:
        print('Errou! Seu palpite foi alto.')
        print('Tente novamente...')
    if jogador < comp:
        print('Errou! Seu palpite foi baixo.')
        print('Tente novamente...')
    if jogador == comp:
        print('-=' * 20)
        print('PARABÉNS! Você acertou!')
        print(f'Eu pensei no número {comp}')
print('-=' * 20)
print(f'Total de tentativas {totjogadas}')
