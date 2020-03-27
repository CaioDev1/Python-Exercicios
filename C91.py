from random import randint
from operator import itemgetter
jogadores = {
    'j1': randint(0, 10),
    'j2': randint(0, 10),
    'j3': randint(0, 10),
    'j4': randint(0, 10)
}
for key, itens in jogadores.items():
    print(f'{key} jogou: {itens}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('RANKING DOS GANHADORES: ')
print(ranking)
