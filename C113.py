def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('ERRO, ENTRADA INVÁLIDA, APENAS NÚMEROS')
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('ERRO, ENTRADA INVÁLIDA, APENAS NÚMEROS')
        else:
            return n


inteiro = leiaint('Digite um valor inteiro: ')
real = leiafloat('Digite um valor real: ')
