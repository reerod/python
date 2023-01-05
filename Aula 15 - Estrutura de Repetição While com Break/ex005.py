#ESTATISTICA EM PRODUTOS
gastos = p_1000 = menor_preco = cont = 0
nome_menor_produto = ''
while True:

    nome = str(input('Informe o nome do produto: ')).strip()
    preco = float(input('Informe o preço: R$ '))
    cont += 1
    gastos += preco
    if preco > 1000:
        p_1000 += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        nome_menor_produto = nome

    perg = ' '
    while perg not in 'SN':
        perg = str(input('Deseja realizar mais alguma compra? [S/N] ')).upper().strip()[0]
    if perg == 'N':
        break

print(f'Total gasto na compra R${gastos:.2f}')
print(f'Totoal de produtos com valor maior que R$1000.00: {p_1000}')
print(f'Produto mais barato foi {nome_menor_produto} que custa R${menor_preco:.2f}')
print('Compra encerrada.')
