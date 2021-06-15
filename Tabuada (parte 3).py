while True:
    número = int(input('Quer tabuada de qual valor?'))
    if número < 0:
        break
    print('=' * 40)
    for c in range (1,11):
        print('{} x {} = {}'.format(número, c, número * c))
    print('=' * 40)
print('FIM DE TABUADA! VOLTE SEMPRE!')