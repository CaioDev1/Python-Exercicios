def aumentar(num, a, show=True):
    aumento = num + (num * a) / 100
    if show:
        return moeda(aumento)
    else:
        return aumento


def diminuir(num, d, show=True):
    diminuido = num - (num * d) / 100
    if show:
        return moeda(diminuido)
    else:
        return diminuido


def dobro(num, show=True):
    dobrado = num * 2
    if show:
        return moeda(dobrado)
    else:
        return dobrado


def metade(num, show=True):
    met = num / 2
    if show:
        return moeda(met)
    else:
        return met


def moeda(num):
    return f'R${num:.2f}'


def resumo(num):
    print(f'-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {num}')
    print(f'Dobro do preço: {dobro(num)}')
    print(f'Metade do preço: {metade(num)}')
    print(f'80% do preço: {aumentar(num, 80)}')
    print(f'35% de redução: {diminuir(num, 35)}')
    print('-' * 30)
