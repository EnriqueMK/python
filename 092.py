from datetime import datetime

atual = datetime.today().year

p = dict()
p['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de Nascimento: '))
p['idade'] = atual - nasc
p['cpts'] = int(input('Carteira de Trabalho (0 não tem): '))
if p['cpts'] > 0:
    p['contratação'] = int(input('Ano de Contratação: '))
    p['salário'] = float(input('Salário R$'))
print('-=' * 30)
print(p)
for k, v in p.items():
    print(f'{k} tem o valor {v}')
