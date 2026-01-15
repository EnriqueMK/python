def title(msg):
    print('-=' * 20)
    print(msg.center(40))
    print('-=' * 20)


title('PROGRESSÃO ARITIMÉTICA COM WHILE')
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
mais = 10
tot = mais
while True:
    cont = 1
    while cont <= mais:
        print(f'{termo} -> ', end='')
        cont += 1
        termo += razao
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
    tot += mais
    if mais == 0:
        break
print(f'Progressão finalizada com {tot} termos mostrados')
