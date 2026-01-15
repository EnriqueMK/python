temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')).strip())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    while True:
        opc = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if opc in 'SN':
            break
    if opc == 'N':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if maior == p[1]:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if menor == p[1]:
        print(f'[{p[0]}]', end='')
