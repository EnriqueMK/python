import random
import time


def title(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


title('JOGO NA MEGA SENA')
jogo = list()
mega = list()
qnt = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= qnt:
    cont = 0
    while True:
        n = random.randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            cont += 1
        if cont == 6:
            break
    jogo.sort()
    mega.append(jogo[:])
    jogo.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {qnt} JOGOS', '-=' * 3)
for i, v in enumerate(mega):
    print(f'Jogo {i+1}: {v}')
    time.sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
