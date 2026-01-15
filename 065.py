soma = cont = maior = menor = 0
while True:
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    cont += 1
    media = soma / cont
    while True:
        opc = str(input('Quer Continuar: [S/N] ')).strip().upper()
        if opc in 'SN':
            break
        else:
            print('\033[31mERRO! Digite apenas S ou N !\033[m')
    if opc == 'N':
        break
print(f'Você digitou {cont} números e a média foi {media}.')
print(f'O maior valor lido foi {maior} e o menor foi {menor}.')