tupla = (int(input('Digite 1° valor: ')),
         int(input('Digite 2° valor: ')),
         int(input('Digite 3° valor: ')),
         int(input('Digite 4° valor: ')))
print('-=' * 20)
print(f'Você digitou os valores: {tupla}')
if 9 in tupla:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
else:
    print('O valor 9 não se encontra na lista!')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}° posição.')
else:
    print('O valor 3 não foi encontrado em nenhuma posição!')
print(f'Os valores pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
