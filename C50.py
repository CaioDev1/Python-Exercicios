soma = 0
for contador in range(0, 6):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        soma += valor
print(f'A soma: {soma}')

