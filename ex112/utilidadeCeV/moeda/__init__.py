def aumentar(preço, taxa=0, frmt=False):
    res = preço + (preço * taxa / 100)
    return res if not frmt else moeda(res)


def diminuir(preço, taxa=0, frmt=False):
    res = preço - (preço * taxa / 100)
    return res if not frmt else moeda(res)


def dobro(preço, frmt=False):
    res = preço * 2
    return res if not frmt else moeda(res)


def metade(preço, frmt=False):
    res = preço / 2
    return res if not frmt else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxa1=0, taxa2=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa1}% de aumento: \t{aumentar(preço, taxa1, True)}')
    print(f'{taxa2}% de redução: \t{diminuir(preço, taxa2, True)}')
    print('-' * 30)
