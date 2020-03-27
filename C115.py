from C115P.interface import *
from C115P.arquivo import *

arq = 'dally.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    escolha = menu()
    if escolha == 1:
        ler_arquivo(arq)
    elif escolha == 2:
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastro(arq, nome, idade)
    elif escolha == 3:
        break
    else:
        print('ERRO, DIGITE UM OPÇÃO VÁLIDA')
print('SISTEMA FINALIZADO')
