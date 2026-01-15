from random import randint


def title(msg):
    print('-=' * 20)
    print(msg.center(40))
    print('-=' * 20)


title('ACERTE O NÚMERO DE 0 A 10')
bot = randint(0, 10)
p = 0
while True:
    n = int(input('Escolha um número de 0 a 10: '))
    if n == bot:
        break
    elif n > bot:
        print('Menos...')
        p += 1
    elif n < bot:
        print('Mais...')
        p += 1
print('-=' * 20)
print('Parabéns...')
print(f'Você acertou com {p} palpites')
print(f'Número gerado pelo computador: {bot}')
