lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('\033[32mValor adicionado com sucesso...\033[m')
    else:
        print('\033[31mValor duplicado! Não vou adicionar...\033[m')
    while True:
        opc = str(input('Quer Continuar? [S/N]: ')).upper().strip()
        if opc in 'SN':
            break
        else:
            print('\033[31mERRO! Digite apenas S ou N !\033[m')
    if opc == 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(lista)}')
