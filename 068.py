from random import randint


def title(msg):
    print('-=' * 20)
    print(msg.center(40))
    print('-=' * 20)


title('VAMO JOGAR PAR OU ÍMPAR')
vitoria = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    while True:
        pi = str(input('Par ou Ímpar [P/I]: ')).strip().upper()
        if pi == 'P' or pi == 'I':
            break
        else:
            print('\033[31mERRO! Digite apenas P ou I !\033[m')
    total = jogador + computador
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}, ', end='')
    if total % 2 == 0:
        print('DEU PAR')
    else:
        print('DEU ÍMPAR')
    print('-' * 30)
    if total % 2 == 0:
        if pi == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitoria += 1
        if pi == 'I':
            print(f'Você PERDEU!')
            break
    elif total % 2 == 1:
        if pi == 'P':
            print('Você PERDEU!')
            break
        if pi == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitoria += 1
    print('-=' * 15)
print('-=' * 15)
print(f'GAME OVER! Você venceu {vitoria} vezes.')
