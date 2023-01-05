'''EX006 - Progressão Aritmética - P.A'''
#fórmula geral de uma P.A
#pa = a + (n - 1) * r
a = int(input('Informe o termo inícial: '))
r = int(input('Informe a razão entre os termos: '))
decimo_termo = a + (11 - 1) * r
for c in range (a, decimo_termo, r):
    print(c, end='.. ')
print('FIM')


