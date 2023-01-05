from time import sleep
print('Legenda: Use "M" para masculino ou "F" para feminino.')
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
print('analisando...')
sleep(1)
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dado incorreto!\n'
                      'Informe os dados conforme as instruções da legenda.\n\n'
                      'Informe novamente seu sexo [M/F]: ')).strip().upper()
    sleep(1)
if sexo == 'M':
    print('Sexo masculino registrado com sucesso.')
if sexo == 'F':
    print('Sexo femino registrado com sucesso.')
