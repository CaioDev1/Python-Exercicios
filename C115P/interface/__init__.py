def cabecalho(titulo):
    print('-' * 42)
    print(titulo.center(42))
    print('-' * 42)


def menu():
    cabecalho('MENU')
    print('1 - VER LISTA DE CADASTRO')
    print('2 - CADASTRAR NOVA PESSOA')
    print('3 - SAIR DO SISTEMA')
    opcao = leiaint('Sua opção: ')
    return opcao


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('ERRO, ENTRADA INVÁLIDA, APENAS NÚMEROS')
        else:
            return n
