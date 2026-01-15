import random
numeros = []


def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(random.randint(0, 10))
    for n in numeros:
        print(f'{n} ', end='')
    print('PRONTO!')


def somaPar():
    soma = 0
    print(f'Somando os valores pares de {numeros}, ', end='')
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'temos {soma}')


sorteia()
somaPar()
