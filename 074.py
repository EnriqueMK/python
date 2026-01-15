from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: ', end='')
maior = menor = 0
for c, n in enumerate(tupla):
    print(n, end=' ')
    if c == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'\nO maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')
