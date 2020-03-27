from C115P.interface import *


def arquivo_existe(arquivo_nome):
    try:
        tentativa = open(arquivo_nome, 'rt')
        tentativa.close()
    except:
        return False
    else:
        return True


def criar_arquivo(arquivo_nome):
    try:
        tentativa = open(arquivo_nome, 'wt+')
        tentativa.close()
    except:
        print('ERRO AO TENTAR CRIAR O ARQUIVO')
    else:
        print(f'Arquivo {arquivo_nome} criado com sucesso.')


def cadastro(arquivo_nome, n='<desconhecido>', i=0):
    try:
        tentativa = open(arquivo_nome, 'at')
        tentativa.write(f'{n};{i}\n')
    except:
        print('ERRO AO TENTAR CADASTRAR PESSOA')
    else:
        print(f'{n} cadastrado com sucesso.')
    finally:
        tentativa.close()


def ler_arquivo(arquivo_nome):
    cabecalho('LISTA DE PESSOAS')
    try:
        tentativa = open(arquivo_nome, 'rt')
    except:
        print('ERRO AO TENTAR LER O ARQUIVO')
    else:
        for itens in tentativa:
            dividido = itens.split(';')
            dividido[1] = dividido[1].replace('\n', '')
            print(f'{dividido[0]} \t\t {dividido[1]}')
    finally:
        tentativa.close()




