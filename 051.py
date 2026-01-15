def title(msg):
    print('=' * 30)
    print(msg.center(30))
    print('=' * 30)


title('10 TERMOS DE UMA PA')
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (11 - 1) * razao
for c in range(primeiro, decimo, razao):
    print(c, end=' -> ')
print('ACABOU!!!')
