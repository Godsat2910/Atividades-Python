número = 0
contador = 0
soma = 0
while True:
    número=int(input('Digite um número:'))
    if número == 999:
        break
    contador = contador + 1
    soma = soma + número
print('Na lista existem {} números e a soma entre eles vale {}.'.format(contador,soma))
print('Fim! Até breve!')