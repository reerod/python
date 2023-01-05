'''EX011 - Analisador Completo'''

soma_idades = 0
idademaisvelho = 0
nomemaisvelho = ''
totalmulheresmenos20 = 0

for p in range (1, 5):
     print('=' * 10)
     nome = str(input('Nome: ')).upper().strip()
     idade = int(input('Idade: '))
     sexo = str(input('Sexo [M/F]: ')).strip()
     soma_idades += idade / 4
     if p == 1 and sexo in 'Mm':
          idademaisvelho = idade
          nomemaisvelho = nome
     if sexo in 'Mm' and idade > idademaisvelho:
          idademaisvelho = idade
          nomemaisvelho = nome
     if sexo in 'Ff' and idade < 20:
          totalmulheresmenos20 += 1
print('='* 10)
print(f'A média de idade do grupo é: {soma_idades:.1f}.')
print(f'O homem mais velho tem {idademaisvelho} e se chama {nomemaisvelho}.')
print(f'O total de mulheres com menos de 20 anos é de {totalmulheresmenos20}.')
