while True:
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('\033[31mDigite apenas M ou F !\033[m')
if sexo == 'M':
    print('Sexo Masculino cadastrado com sucesso!')
elif sexo == 'F':
    print('Sexo Feminino cadastrado com sucesso!')
