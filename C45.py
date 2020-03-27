from random import choice
print('1 - pedra \n 2 - papel \n 3 - tesoura')
player_op = str(input('Sua opção: ')).lower()
computer_op = choice(['pedra', 'papel', 'tesoura'])
if player_op == 'pedra' and computer_op == 'tesoura':
    print(f'Você {player_op} \n o computador: {computer_op} \n VOCÊ VENCEU!')
elif player_op == 'papel' and computer_op == 'pedra':
    print(f'Você {player_op} \n o computador: {computer_op} \n VOCÊ VENCEU!')
elif player_op == 'tesoura' and computer_op == 'papel':
    print(f'Você {player_op} \n o computador: {computer_op} \n VOCÊ VENCEU!')
elif player_op == computer_op:
    print(f'Você {player_op} \n o computador: {computer_op} \n EMPATE!')
else:
    print(f'Você {player_op} \n o computador: {computer_op} \n VOCÊ PERDEU!')
