numeros = []
for contador in range(0, 5):
    numeros.append(int(input('Digite um valor para a lista: ')))
print(f'Maior valor digitado: {max(numeros)} - posição {numeros.index(max(numeros))}')
print(f'Menor valor digitador: {min(numeros)} - posição {numeros.index(min(numeros))}')
