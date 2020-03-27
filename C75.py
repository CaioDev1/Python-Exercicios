numeros = int(input('Numero 1: ')), int(input('Numero 2: ')), int(input('Numero 3: ')), int(input('Numero 4: ')), int(input('Numero 5: '))
print(f'Quantas vezes o número 9 apareceu: {numeros.count(9)}')
print(f'Em que posição foi digitado o primeiro valor 3: {numeros.index(3)}')
print(f'Valores pares: ', end='')
for valores in numeros:
    if valores % 2 == 0:
        print(valores, end=' ')
