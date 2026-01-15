def voto(nasc):
    import datetime
    atual = datetime.datetime.today().year
    idade = atual - nasc
    if 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBIRGATÓRIO.'
    elif idade == 16 or idade == 17 or idade >= 66:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'


print('-' * 30)
print(voto(int(input('Em que ano você nasceu? '))))