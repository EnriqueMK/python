def title(msg):
    print('-=' * 20)
    print(msg.center(40))
    print('-=' * 20)


title('PROGRESSÃO ARITIMÉTICA COM WHILE')
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    cont += 1
    termo += razao
print('FIM!')
