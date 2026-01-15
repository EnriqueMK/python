ficha = []
media = 0
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    while True:
        opc = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if opc in 'SN':
            break
        else:
            print('\033[31mERRO! Digite apenas S ou N !\033[m')
    if opc == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, v in enumerate(ficha):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')
print('-' * 40)
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc >= len(ficha):
        print('\033[31mERRO! Não existe aluno com esse código !\033[m')
    else:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

