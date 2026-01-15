import time
import datetime


def title(msg):
    print('-=' * 15)
    print(msg.center(30))
    print('-=' * 15)


def linha1():
    print('-' * 30)


title('CADASTRO DE PESSOAS')
pessoa = {}
galera = []
atual = datetime.datetime.today().year
soma = cont = maior = menor = 0
while True:
    cont += 1
    print(f'{f"{cont}° PESSOA":^30}')
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if pessoa['sexo'] == 'M' or pessoa['sexo'] == 'F':
            break
        else:
            print('\033[31mERRO! Digite apenas M ou F !\033[m')
    ano = int(input('Em que ano você nasceu? '))
    idade = atual - ano
    pessoa['idade'] = idade
    soma += idade
    pessoa['peso'] = float(input('Peso: '))
    pessoa['altura'] = float(input('Altura (m): '))
    galera.append(pessoa.copy())
    pessoa.clear()
    while True:
        opc = str(input('Deseja continuar? ')).strip().upper()
        if opc in 'SN':
            break
        else:
            print('\033[31mERRO! Digite apenas S ou N !\033[m')
    linha1()
    if opc == 'N':
        break
media = soma / len(galera)
print('-=' * 30)
time.sleep(1)
print(f'- O grupo tem {len(galera)} pessoas.')
time.sleep(1)
print(f'- A média de idade é {media:.2f} anos.')
time.sleep(1)
print(f'- Pessoas maiores de idade: ')
for p in galera:
    if p['idade'] >= 18:
        time.sleep(1)
        print(f'[ {p["nome"]} com {p["idade"]} anos ]')
time.sleep(1)
print(f'- As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        time.sleep(1)
        print(f'[{p["nome"]}] ', end='')
time.sleep(1)
print(f'\n- Lista das pessoas que estão acima da média:')
print()
for p in galera:
    if p['idade'] > media:
        time.sleep(1)
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print()
time.sleep(1)
print(f'- Lista das pessoas mais pesadas e mais leves:')
time.sleep(1)
for i, p in enumerate(galera):
    if i == 0:
        maior = menor = p['peso']
    else:
        if p['peso'] > maior:
            maior = p['peso']
        if p['peso'] < menor:
            menor = p['peso']
print('Pessoas mais pesadas:')
for p in galera:
    if maior == p['peso']:
        time.sleep(1)
        print(f'[ {p["nome"]} com {maior}Kg ] ')
time.sleep(1)
print()
print('Pessoas mais leves:')
for p in galera:
    if menor == p['peso']:
        time.sleep(1)
        print(f'[ {p["nome"]} com {menor}Kg ] ')
time.sleep(1)
print()
print('- Lista de pessoas maiores e menores que 1.60cm:')
time.sleep(1)
print('Pessoas maiores que 1.60cm:')
for p in galera:
    if p['altura'] >= 1.60:
        time.sleep(1)
        print(f'[ {p["nome"]} com {p["altura"]}cm ]')
time.sleep(1)
print('Pessoas menores que 1.60cm:')
for p in galera:
    if p['altura'] <= 1.60:
        time.sleep(1)
        print(f'[ {p["nome"]} com {p["altura"]}cm ]')
time.sleep(1)
print('\n<<< ENCERRADO >>>')
