import time


def contador(i, f, p):
    print('-=' * 20)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            time.sleep(0.3)
            cont += p
        print('FIM!')
    if f < i:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            time.sleep(0.3)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim   : '))
pas = int(input('Passo : '))
contador(ini, fim, pas)