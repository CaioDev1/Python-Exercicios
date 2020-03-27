numeros = []
par = []
impar = []
while True:
    valor = int(input('Valor para a lista: '))
    numeros.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    continuar = str(input('Continuar? (s/n): ')).lower().strip()
    if continuar == 'n':
        break
print(numeros)
print(f'Lista dos n° pares: {par}')
print(f'Lista dos n° ímpares: {impar}')
