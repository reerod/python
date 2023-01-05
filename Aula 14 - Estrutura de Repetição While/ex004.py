#FATORIAL DE UM NUMERO

num = int(input('Informe um numero e saiba o seu fatorial: '))
fatorial = 1
cont = 1
while cont <= num:
    fatorial = fatorial * cont
    cont += 1
print(f'O fatorial de {num}! é {fatorial}')
