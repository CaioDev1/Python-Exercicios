def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('ERRO, ENTRADA INVÁLIDA, APENAS NÚMEROS')
        else:
            return n


numero = leiaint('Digite um número: ')
