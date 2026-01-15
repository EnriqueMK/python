def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(len(linha())-1))
    print(linha())


def leiaInt(valor):
    while True:
        try:
            n = int(input(valor))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            break
        else:
            return n


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[93m{c} -\033[m \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
