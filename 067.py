def title(msg):
    print('=' * 20)
    print(msg.center(20))
    print('=' * 20)


title('MOSTRAR TABUADA')
while True:
    n = int(input('Escolha um número \npara mostrar sua tabuada: '))
    if n < 0:
        break
    cont = 1
    print('=' * 20)
    while cont <= 10:
        print(f'{n} x {cont:>2} = {n*cont}')
        cont += 1
    print('=' * 20)
print('Obrigado por usar nosso programa. Volte sempre!')
