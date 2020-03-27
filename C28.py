from random import randint
computer = randint(0, 5)
player_op = int(input('Digite um valor de 0 a 5: '))
if player_op == computer:
    print(f'Computador: {computer} \n Você: {player_op} \n VOCÊ VENCEU!')
else:
    print(f'Computador: {computer} \n Você: {player_op} \n VOCÊ PERDEU!')
