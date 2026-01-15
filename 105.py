def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situação de vários alunos.
    :param num: uma ou mais notas dos alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar.
    :return: dicionário com várias informações sobre a turma.
    '''
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num)/len(num)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 1.5, True)
print(resp)
help(notas)
