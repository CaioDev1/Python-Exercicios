from random import randint
vitorias = 0
while True:
    par_impar = str(input('P/ I: ')).lower().strip()
    player_op = int(input('Digite um número: '))
    computer_op = randint(0, 10)
    if par_impar == 'p':
        if (player_op + computer_op) % 2 == 0:
            print(f'Você: {player_op} \n computador: {computer_op} \n PAR! VOCÊ VENCEU')
            vitorias += 1
        else:
            print(f'Você: {player_op} \n computador: {computer_op} \n ÍMPAR! VOCÊ PERDEU')
            break
    else:
        if (player_op + computer_op) % 2 != 0:
            print(f'Você: {player_op} \n computador: {computer_op} \n ÍMPAR! VOCÊ VENCEU')
            vitorias += 1
        else:
            print(f'Você: {player_op} \n computador: {computer_op} \n PAR! VOCÊ PERDEU')
            break
print(f'Quantidade de vitórias: {vitorias}')
print('FINALIZADO')


