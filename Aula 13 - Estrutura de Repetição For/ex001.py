'''Ex001 - Contagem Regressiva'''
from time import sleep
for cont in range (10, 0, -1):
    print(cont, end='.. ')
    sleep(1)
print('\n!!!BOOM!!!')