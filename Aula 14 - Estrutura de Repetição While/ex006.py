#TRATANDO VÁRIOS VALORES
somador = 0
contador = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    somador += num
    contador += 1
    num = int(input('Digite um numero [999 para parar]: '))
print(f'Você digitou {contador} números e a soma entre eles foi {somador}')
