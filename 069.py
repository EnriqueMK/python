def title(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


title('CADASTRE UMA PESSOA')
mais18 = homem = menos20 = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        mais18 += 1
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('\033[31mERRO! Digite apenas M ou F !\033[m')
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        if idade < 20:
            menos20 += 1
    while True:
        print('-' * 30)
        opc = str(input('Quer continuar ? [S/N]: ')).strip().upper()
        print('-' * 30)
        if opc in 'SN':
            break
        else:
            print('\033[31mERRO! Digite apenas S ou N !\033[m')
    if opc == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
if homem > 1:
    print(f'Ao todo temos {homem} homens cadastrados.')
else:
    print(f'Ao todo temos {homem} homem cadastrado.')
if menos20 > 1:
    print(f'E temos {menos20} mulheres com menos de 20 anos.')
else:
    print(f'E temos {menos20} mulher com menos de 20 anos.')
