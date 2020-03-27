from C107P import moeda


def leia_dinheiro(msg):
    while True:
        try:
            dinheiro = int(input(msg))
        except (ValueError, TypeError):
            print(f'ERRO, VALOR NÃO É UM NÚMERO.')
        else:
            dinheiro = moeda.moeda(dinheiro)
            return dinheiro
