from random import randint
from time import sleep
jogos = []
n_jogos = int(input('Digite o número de jogos gerados: '))
for contador in range(0, n_jogos):
    jogos.append([])
    for contador2 in range(0, 6):
        jogos[contador].append(randint(1, 60))
for contador in range(0, n_jogos):
    print(f'Jogo {contador + 1}: {jogos[contador]}')
    sleep(0.5)
