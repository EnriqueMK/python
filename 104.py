def leiaInt(valor):

    while True:
        n = str(input(valor))
        if n.isnumeric():
            int(n)
            break
        else:
            print('\033[31mERRO! Só aceitamos valores inteiros.\033[m')
    return n


print('-' * 30)
n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')
