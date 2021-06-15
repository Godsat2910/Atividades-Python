from random import randint
vitória = 0
while True:
    print('=' * 40)
    jogador = int(input('Digite um número:'))
    computador = randint(0,11)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar?[P/I]')).strip().upper()[0]
    print('Você jogou {} e o computador jogou {}. Logo, a soma deu {}.'.format(jogador,computador,total))
    if escolha == 'P':
        if total % 2 == 0:
            print('PAR!')
            print('VOCÊ GANHOU!')
            vitória = vitória + 1
        else:
            print('ÍMPAR!')
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
             print('ÍMPAR!')
             print('VOCÊ VENCEU!')
             vitória = vitória + 1
        else:
             print('PAR!')
             print('VOCÊ PERDEU!')
             break
    print('Jogue de novo....')
print('ACABOU! Você venceu {} vezes.'.format(vitória))