def aumentar(preço, taxa=0, frmt=False):
    res = preço + (preço * taxa / 100)
    return res if not frmt else moeda(preço)


def diminuir(preço, taxa=0, frmt=False):
    res = preço - (preço * taxa / 100)
    return res if not frmt else moeda(preço)


def dobro(preço, frmt=False):
    res = preço * 2
    return res if not frmt else moeda(preço)


def metade(preço, frmt=False):
    res = preço / 2
    return res if not frmt else moeda(preço)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')



