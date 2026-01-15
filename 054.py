from datetime import datetime

atual = datetime.today().year
maior = menor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if atual - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemso {maior} pessoas maiores de idade.')
print(f'E também tivemos {menor} pessoas menores de idade.')
