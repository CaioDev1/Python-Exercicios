matriz = [[], [], []]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input('Digite um valor para a matriz: ')))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
