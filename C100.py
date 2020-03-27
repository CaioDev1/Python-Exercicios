from random import randint


def sorteia(n):
    for contador in range(0, 5):
        n.append(randint(0, 10))


def soma_par(n):
    soma = 0
    for itens in n:
        if itens % 2 == 0:
            soma += itens


numeros = []
sorteia(numeros)
print(numeros)
soma_par(numeros)
print(numeros)

