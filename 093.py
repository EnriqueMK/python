j = dict()
g = list()
j['jogador'] = str(input('Nome do Jogador: ')).strip()
qnt = int(input(f'Quantas partidas {j["jogador"]} jogou? '))
for c in range(0, qnt):
    g.append(int(input(f'Quantos gols na partida {c}? ')))
j['gols'] = g
j['total'] = sum(g)
print('-=' * 30)
print(j)
print('-=' * 30)
for k, v in j.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {j["jogador"]} jogou {qnt} partidas.')
for i, v in enumerate(g):
    print(end='     ')
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {qnt} gols.')
