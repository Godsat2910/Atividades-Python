soma = 0
maiorde1000 = 0
contador = 0
maior = 0
menor = 0
while True:
    produto = str(input('Nome do produto:')).strip()
    custo = float(input('Quanto custa o produto?'))
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()
    contador = contador + 1
    soma = soma + custo
    if custo > 1000:
        maiorde1000 = maiorde1000 + 1
    if contador != 1:
        if produto > maior:
            maior = produto
        elif produto < menor:
            menor = produto
    else:
        maior = produto
        menor = produto
    if escolha == 'N':
        break
print('O total gasto na compra é de R$ {:.2f}'.format(soma))
print('{} produtos estão acima de R$ 1000,00.'.format(maiorde1000))
print('O nome do produto mais barato se chama: {}'.format(menor))
print('Fim do programa!')