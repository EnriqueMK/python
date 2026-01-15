frase = str(input('Digite um frase: ')).upper().strip().replace(' ', '')
inverso = frase[::-1]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('A frase digitada É UM PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')
