bra = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
       'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
       'Atlético', 'BotaFogo', 'Atlético-PR', 'Bahia',
       'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
       'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {bra}')
print('-=' * 20)
print(f'Os 5 primeiros são {bra[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {bra[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(bra)}')
print('-=' * 20)
print(f'O Chapecoense está na {bra.index("Chapecoense")+1}° posição')
