def ajuda(comando):
    while True:
        opc = str(input(comando))
        try:
            print(help(opc))
        except:
            print('ERRO AO DIGITAR COMANDO, REINSIRA')
        else:
            continuar = str(input('Quer continuar? (s/n): ')).lower().strip()
            if continuar == 'n':
                break


ajuda('Digite o comando para ver a instrução: ')
print('FINALIZADO')
