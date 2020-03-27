matriz = [[], [], []]
soma_p = 0
soma_c3 = 0
maior_l2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Digite um valor para a matriz: [{linha}][{coluna}]: ')))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            soma_p += matriz[linha][coluna]
        if coluna == 2:
            soma_c3 += matriz[linha][2]
    print()
maior_l2 = max(matriz[1])
print(f'A soma dos valores pares: {soma_p}')
print(f'A soma dos valores na terceira coluna: {soma_c3}')
print(f'O maior valor da segunda linha: {maior_l2}')
