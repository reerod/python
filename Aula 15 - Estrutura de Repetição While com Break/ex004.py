#ANÁLISE DE DADOS DO GRUPO
from time import sleep
maior_idade = 0
tot_homens = 0
mulheres_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if idade >= 18:
        maior_idade += 1
    if sexo == 'M':
        tot_homens += 1
    if idade < 20 and sexo == 'F':
        mulheres_20 += 1
    while sexo != 'M' and sexo != 'F':
        print('Dado inválido.. Tente novamente usando M ou F')
        sexo = str(input('Sexo: ')).upper().strip()
    perg = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while perg != 'S' and perg != 'N':
        print('Resposta inválida.. Tente novamente')
        perg = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if perg == 'N':
            break
print('\nAnalisando dados do grupo...')
sleep(1)
print(f'\nTemos o total de {maior_idade} pessoas cadastradas maiores de 18.')
print(f'Temos o total de {tot_homens} homens cadastrados.')
print(f'Temos o total de {mulheres_20} mulheres com menos de 20 anos.')
print('Programa encerrado.')
