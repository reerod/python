'''r = 'S'
somador = 0
while r == 'S':
    for p in range(1, 5):
        n = int(input('Digite um numero: '))
        somador += n
    r = str(input('Quer continuar? [S/N]: ')).upper()
print(f'Resultado da soma dos números {somador}')
print('Fim')'''

'''turma = 1
pergunta = int(input('Quantos alunos tem na turma? '))
while turma < pergunta+1:
    nomealunos = str(input(f'Nome do {turma}ª aluno: ')).strip()
    turma += 1
print('Agora vamos às notas...')'''

'''#FATORIAL DE UM NUMERO COM WHILE
num = int(input('Informe um numero e saiba o seu fatorial: '))
fatorial = 1
cont = 1
while cont <= num:
    fatorial = fatorial * cont
    cont += 1
print(fatorial)'''

'''#FATORIAL DE UM NUMERO COM FOR

num = int(input('Informe um numero e saiba o seu fatorial: '))

fatorar = 1
for cont in range(num, 0, -1):
    fatorar *= cont
    print(cont, end=' ')
print(fatorar)'''

'''#OS 10 PRIMEIROS TERMOS DE UMA PROGRESSAO ARITMETICA

primeirotermo = int(input('Defina o início: '))
razao = int(input('Agora, defina a razão da PA: '))
termo = primeirotermo
cont = 1
total = 0 #variavel para o total de termos que se repetem, funciona como um limite de repetição (ex. 10 repetições)
maistermos = 10 #recebe o valor 10 pois temos que mostrar os 10 primeiros termos para o usuario
while maistermos != 0:
    total = total + maistermos
    while cont <= total:
        print(termo, end=' ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    maistermos = int(input('Quantos termos deseja mostrar a mais? '))

print(f'SOMA: {total}')
'''

'''primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeirotermo
cont = 1
total = 0 #tem duas funções: de termo determinado, que quando somado com a variavel p, assume o valor 10; e de contador,
#quando precisamos saber a quantidade de termos repetidos durante a execução do codigo.
p = 10 #determina a quantidade de termos iniciais a serem exibidos

while p != 0:
    total = total + p
    while cont <= total:
        print(termo, end=' ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    p = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'Quantidade de termos: {total}')'''

'''somador = 0
num = 0
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    somador += num
print(f'{somador-999}')'''


