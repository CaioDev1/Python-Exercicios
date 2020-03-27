numeros = []
for contador in range(0, 5):
    if contador == 0:
        numeros.append(int(input('Digite um valor para a lista: ')))
    else:
        valor = int(input('Digite um valor para a lista: '))
        if valor > numeros[contador - 1]:
            numeros.append(valor)
        else:
            for ind, itens in enumerate(numeros):
                if valor < itens:
                    numeros.insert(ind, valor)
                    break
    print(numeros)
