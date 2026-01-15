def leiaDinheiro(valor):
    while True:
        n = str(input(valor))
        if n.isnumeric():
            return float(n)
        else:
            print(f'\033[31mERRO! "{n}" é um preço inválido!\033[m')

