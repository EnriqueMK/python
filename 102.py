def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param n: Número a ser calculado.
    :param show: (Opcional). Mostra a conta.
    :return: Retorna o valor de n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, True))
help(fatorial)
