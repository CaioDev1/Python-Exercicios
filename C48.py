soma = 0
for contador in range(0, 500, 3):
    if contador % 2 != 0:
        soma += contador
        print(contador, end=' -> ')
print(f'A soma é: {soma}')
