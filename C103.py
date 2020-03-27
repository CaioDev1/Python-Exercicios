def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols.')


nome = str(input('Nome: ')).lower().strip()
gols = str(input('Número de gols: '))
if nome == '':
    ficha(g=gols)
else:
    if gols == '':
        ficha(nome)
    else:
        ficha(nome, gols)
