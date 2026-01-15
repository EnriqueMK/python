def title(msg):
    print('=' * 40)
    print(msg.center(40))
    print('=' * 40)


title('LOJA SUPER BARATÃO')
compra = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    compra += preco
    if preco >= 1000:
        totmil += 1
    if cont == 0:
        menor = preco
        barato = produto
    elif preco < menor:
        menor = preco
        barato = produto
    cont += 1
    while True:
        opc = str(input('Quer Continuar? [S/N]: ')).strip().upper()
        if opc in 'SN':
            break
        else:
            print('\033[31mDigite apenas S ou N !\033[m')
    if opc == 'N':
        break
print('-' * 15, 'FIM DO PROGRAMA', '-' * 15)
print(f'O total da compra foi de R${compra:.2f}')
print(f'Temos {totmil} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}.')
