jogador = {}
partida = []
time = []
while True:
    print('-' * 30)
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partida.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    jogador.clear()
    partida.clear()
    while True:
        opc = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if opc in 'SN':
            break
        print('\033[31mERRO! Digite apenas S ou N !\033[m')
    if opc == 'N':
        break
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    dados = int(input('Mostrar dados de qual jogador? '))
    if dados == 999:
        break
    if dados >= len(time):
        print(f'\033[31mERRO! Não existe jogador com esse código {dados}\033[m')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[dados]["nome"]}:')
        for i, g in enumerate(time[dados]['gols']):
            print(f'    No jogo {i} fez {g} gols.')
        print('-' * 40)
print('<<< VOLTE SEMPRE >>>')

