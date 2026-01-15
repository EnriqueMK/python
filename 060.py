n = int(input('Digite um número \npara ver seu fatorial: '))
f = 1
cont = 1
print(f'{n}! = ', end='')
while True:
    if cont < n:
        print(f'{cont} x ', end='')
        cont += 1
        f *= cont
    else:
        print(f'{cont} = {f}', end='')
        break
