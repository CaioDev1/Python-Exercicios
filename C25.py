nome = str(input('Nome: ')).lower().strip().split()


def existe_silva(nome_):
    for palavras in nome_:
        if palavras == 'silva':
            return True


if existe_silva(nome):
    print('Existe Silva no nome? SIM')
else:
    print('Existe Silva no nome? NÃO')
