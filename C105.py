info = {}


def notas(* n, sit=False):
    """

    :param n: lista com as notas
    :param sit: mostra a situação da média da sala
    :return: sem retorno
    """
    soma = 0
    info['quantidade'] = n
    info['maior'] = max(info['quantidade'])
    info['menor'] = min(info['quantidade'])
    for itens in info['quantidade']:
        soma += itens
    info['media'] = soma / len(info['quantidade'])
    if info['media'] > 6:
        info['situacao'] = 'BOA'
    else:
        info['situacao'] = 'RUIM'
    print(info)


notas(3, 4, 6, 1, 5, 7, sit=True)
