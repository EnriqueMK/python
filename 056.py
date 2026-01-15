def title(msg):
    print('=' * 30)
    print(msg.center(30))
    print('=' * 30)


title('CADASTRO DE PESSOAS')
soma = maisvelho = maior = menos20 = 0
for c in range(0, 4):
    print('-' * 5, f'{c+1}° PESSOA', '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    soma += idade
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('\033[31mERRO! Digite apenas M ou F !\033[m')
    if sexo == 'M':
        if c == 0:
            maior = idade
            maisvelho = nome
        elif idade > maior:
            maior = idade
            maisvelho = nome
    if sexo == 'F':
        if idade < 20:
            menos20 += 1
media = soma / 4
print('-=' * 20)
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maior} anos e se chama {maisvelho}.')
print(f'Ao todo são {menos20} mulheres com menos de 20 anos.')
