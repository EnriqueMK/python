import time


def titulo(msg):
    t = len(msg) + 2
    print('~' * t)
    print(msg.center(t))
    print('~' * t)


while True:
    print('\033[7;49;32m', end='')
    titulo('SISTEMA DE AJUDA PyHELP')
    print('\033[m', end='')
    cmd = str(input('Função ou Biblioteca > ')).strip()
    if cmd == 'FIM':
        break
    print('\033[7;49;36m', end='')
    titulo(f"Acessando o manual do comando '{cmd}'")
    print('\033[m', end='')
    time.sleep(1)
    print('\033[7;49;39m')
    help(cmd)
    print('\033[m')
    time.sleep(1)

