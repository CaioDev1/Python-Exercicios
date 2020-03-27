numeros = [[], []]
for contador in range(0, 7):
    numeros.append(int(input('Digite um valor para a lista: ')))
    if numeros[contador] % 2 == 0:
        numeros[0].append(numeros[contador])
    else:
        numeros[1].append(numeros[contador])
print(f'A lista dos valores pares: {numeros[0]}')
print(f'A lista dos valores ímpares: {numeros[1]}')
