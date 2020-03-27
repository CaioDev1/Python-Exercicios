n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
print('1 - somar \n 2 - multiplicar \n 3 - maior \n 4 - novos números \n 5 - sair do programa')
opcao = int(input('Sua opção: '))
while opcao != 5:
    if opcao == 1:
        print(f'A soma é: {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação é: {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é o maior número')
        elif n1 == n2:
            print('Os valores são iguais')
        else:
            print(f'{n2} é o maior número')
    elif opcao == 4:
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor 2: '))
    elif opcao == 5:
        break
    else:
        print('DIGITE UM NÚMERO VÁLIDO')
print('FINALIZADO.')
