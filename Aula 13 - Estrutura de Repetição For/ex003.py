'''EX003 - Ímpares Múltiplos de 3'''
contador = 0
somador = 0
for i in range (0,501):
    if i % 3 == 0 and i % 2 == 1:
        contador += 1
        somador += i
print(f'O resultado da soma dos '
      f'{contador} valores múltiplos de 3 é {somador}.')
print('FIM.')