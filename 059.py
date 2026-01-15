n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

while True:
    print('=' * 30)
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
    print('=' * 30)
    opc = int(input('Escolha uma opção: '))
    if opc == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    if opc == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    if opc == 3:
        if n1 > n2:
            print(f'O maior número é o {n1}')
        else:
            print(f'O maior número é o {n2}')
    if opc == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    if opc == 5:
        break
print(f'Obrigado por usar nosso programa. Volte sempre!')
