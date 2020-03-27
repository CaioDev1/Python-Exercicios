maior = 0
menor = 0
for contador in range(0, 5):
    peso = float(input('Peso: '))
    if contador == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi: {maior}')
print(f'O menor peso foi: {menor}')
