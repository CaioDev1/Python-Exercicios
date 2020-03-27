from random import randint
player_op = int(input('Digite um número de 0 a 10: '))
computer_op = randint(0, 10)
tentativas = 1
while player_op != computer_op:
    print('ERRADO, TENTE DENOVO')
    player_op = int(input('Digite um número de 0 a 10: '))
    tentativas += 1
print(f'VITÓRIA! N° DE TENTATIVAS: {tentativas}')
