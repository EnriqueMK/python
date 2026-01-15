import random
import time
import operator


def tittle(msg):
    print(f'{msg}:')


jogo = dict()
rank = dict()
tittle('Valores sortedos')
for c in range(1, 5):
    jogo[f'jogador{c}'] = random.randint(1, 10)
for k, v in jogo.items():
    print(end='    ')
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)
rank = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
tittle('Ranking dos jogadores')
for i, v in enumerate(rank):
    print(end='    ')
    time.sleep(1)
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
