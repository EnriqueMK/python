matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = tcoluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        tcoluna += matriz[l][2]
        if l == 1:
            maior = matriz[1][c]
        elif matriz[1][c] > maior:
            maior = matriz[1][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[l][c]}  ]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}.')
print(f'A soma dos valores da terceira coluna é {tcoluna}.')
print(f'O maior valor da segunda linha é {maior}.')
