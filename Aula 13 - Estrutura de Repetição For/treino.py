somaidade = 0
nomehomemmaisvelho = ''
idadehomemmaisvelho = 0
for i in range(1, 5):
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaidade += idade
    if i == 1 and sexo in 'M':
        nomehomemmaisvelho = nome
        idadehomemmaisvelho = idade
    if idade > idadehomemmaisvelho and sexo in 'M':
        idadehomemmaisvelho = idade
        nomehomemmaisvelho = nome
media = somaidade / 4
print(f'Média das idades: {media}')
print(f'O homem mais velho se chama {nomehomemmaisvelho} e '
      f'tem {idadehomemmaisvelho} anos.')
