quantidade = 0
soma = 0
while True:
    n = int(input('Digite um número (999 finaliza): '))
    if n == 999:
        break
    else:
        quantidade += 1
        soma += n
print(f'A quantidade de valores inseridos: {quantidade}')
print(f'A soma dos valores: {soma}')
