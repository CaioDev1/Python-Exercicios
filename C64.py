quantidade = 1
soma = 0
num = int(input('Número (999 finaliza): '))
while num != 999:
    num = int(input('Número (999 finaliza): '))
    quantidade += 1
    soma += num
print(f'A soma dos valores foi: {soma}')
print(f'O quantidade de números foi: {quantidade}')
