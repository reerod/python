#TRATANDO VARIOS NUMEROS - COM FLAG
num = cont = somador = 0
while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    somador += num
print(f'Você digitou {cont} números e a soma entre eles foi {somador}!')
