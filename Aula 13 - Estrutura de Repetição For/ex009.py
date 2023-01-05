'''EX009 - Grupo da Maioridade'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range (1, 5):
    ano = int(input(f'Informe o ano em que a {i}ª pessoa '
                    f'nasceu: '))
    idade = atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade'
      f' e {totmenor} menores de idade')