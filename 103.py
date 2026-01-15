def ficha(nome='<desconhecido>', gols=0):
    '''
    -> Ve quem e quantos gols fizeram no campeonato.
    :param nome: Lê o nome.
    :param gols: Lê a quantidade de gols.
    :return: Sem retorno.
    '''
    print(f'Jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 30)
n = str(input('Nome do Jogador: ')).strip()
g = str(input('Número de gols: ')).strip()
if g.isalnum():
    int(n)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
help(ficha)
