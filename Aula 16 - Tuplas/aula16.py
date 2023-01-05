lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
'''#MANIPULANDO A TUPLA
print(lanche[1])
print(lanche[3])
#DIREITA P/ A ESQUERDA
print(lanche[-1])
print(lanche[-2])
#FATIANDO A TUPLA
print(lanche[0:])
print(lanche[1:3])
print(lanche[:4])
print(lanche[-3:])
print(lanche)'''
'''#MOSTRANDO ITENS DA TUPLA DE VARIAS MANEIRAS
#TERCEIRA MANEIRA COM FOR MOSTRANDO A POSIÇÃO:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos} ') #quando quisermos mostrar a posição sem o len()
#SEGUNDA MANEIRA UTILIZANDO len():
#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #quando quisermos mostrar a posição
#PRIMEIRA MANEIRA UTILIZANDO FOR:
#for comida in lanche:
#    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')'''
'''#MOSTRANDO OS ITENS EM ORDEM ALFABETICA COM O METODO sorted()
print(sorted(lanche))
print(lanche)'''
'''#CONCATENAÇÃO DE TUPLAS
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c)) #QUANTIDADE DE ELEMENTOS
print(c.count(5)) #QUANTAS VEZES APARECE O ELEMENTO, POR EX O NUMERO 5
print(c.index(8)) #MOSTRA A POSIÇÃO DO ELEMENTO, POR EX O NUMERO 8
print(c.index(5, 1)) #POSIÇÃO DE UM ELEMENTO REPETIDO, POR EX O NUMERO 2 QUE ESTA EM DUAS POSIÇÕES
print(sorted(c)) #TUPLE EM ORDEM CRESCENTO COM O METODO sorted()'''
#TUPLAS SUPORTAM ITENS VARIADOS
pessoa = ('Renan', 23, 'M', 70.00)
del(pessoa) #EXCLUI A TUPLA INTEIRA
print(pessoa)
