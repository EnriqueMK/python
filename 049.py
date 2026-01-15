from time import sleep


def title(msg):
    print('=' * 30)
    print(msg.center(30))
    print('=' * 30)


title('TABUADA')
n = int(input('Escolha um número \npara ver sua tabuada: '))
print('=-' * 10)
for c in range(1, 11):
    print(f'{n} x {c:<2} = {n*c}')
print('=-' * 10)
