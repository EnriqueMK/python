def title(msg):
    print('=' * 30)
    print(msg.center(30))
    print('=' * 30)


maior = menor = 0
title('MAIOR E MENOR PESO')
for c in range(0, 5):
    peso = float(input(f'Peso da {c+1}° pessoa: '))
    if c == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'E o menor peso lido foi de {menor}Kg')
