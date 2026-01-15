lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        opc = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if opc in 'SN':
            break
        else:
            print('\033[31mDigite apenas S ou N !\033[m')
    if opc == 'N':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
