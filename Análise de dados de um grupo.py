print('{:=^60}'.format('ANÁLISE DE DADOS'))
menosde20anos = 0
homens = 0
maiordeidade = 0
while True:
    idade = int(input('A idade?'))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('O sexo?[F/M]')).strip().upper()[0]
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('=' * 60)
    if idade >= 18:
        maiordeidade = maiordeidade + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F':
        if idade < 20:
            menosde20anos = menosde20anos + 1
    if resposta == 'N':
        break
print('Nesse grupo existem {} pessoas que são de maior.'.format(maiordeidade))
print('Temos {} homens cadastrados.'.format(homens))
print('{} mulheres têm menos de 20 anos.'.format(menosde20anos))
print('FIM DO PROGRAMA!')