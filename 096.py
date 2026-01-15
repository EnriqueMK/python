def area(l, c):
    t = l * c
    print(f'A área de um terreno {l}x{c} é de {t}².')


print(' Controle de Terrenos:')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
