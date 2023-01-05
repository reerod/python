'''EX010 - Maior e Menor da Squencia'''

p_maior = 0
p_menor = 0
for i in range (1, 5):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        p_maior = peso
        p_menor = peso
    else:
        if peso > p_maior:
            p_maior = peso
        if peso < p_menor:
            p_menor = peso
print(f'O maior peso informado foi {p_maior:.2f}Kg e'
      f' o menor peso informado foi {p_menor:.2f}Kg')
