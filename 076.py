def title(msg):
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)


lista = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
title('LISTAGEM DE PREÇOS')
for i, v in enumerate(lista):
    if i % 2 == 0:
        print(f'{v:.<30}', end='')
    else:
        print(f'R${v:>7.2f}')
print('-' * 40)