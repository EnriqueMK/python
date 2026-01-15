lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        opc = str(input('Quer Continuar? [S/N]: ')).upper().strip()
        if opc in 'SN':
            break
        else:
            print('\033[31mERRO! Digite apenas S ou N !\033[m')
    if opc == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)+1} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
