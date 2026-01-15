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


def leiaFloat(valor):
    while True:
        try:
            n = float(input(valor))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido!\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            break
        else:
            return n


i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')

