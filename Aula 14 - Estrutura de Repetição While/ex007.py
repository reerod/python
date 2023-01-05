#Maior e Menor valores
op = ''
cont = 0
maior = 0
menor = 0
while op != 'N':
    num = int(input('Digite um numero: '))
    op = str(input('Quer continuar? [S/N] ')).upper().strip()
    if num == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    else:
        menor = num
    cont = cont + 1
print(maior, menor)
