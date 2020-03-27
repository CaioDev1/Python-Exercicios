n = int(input('Digite um número: '))
soma = n
maior = n
menor = n
quantidade = 1
continuar = str(input('Quer continuar? (s/n): ')).lower().strip()
while continuar != 'n':
    n = int(input('Digite um número: '))
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    continuar = str(input('Quer continuar? (s/n): ')).lower().strip()
    quantidade += 1
print(f'A média é: {soma / quantidade }')
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')
