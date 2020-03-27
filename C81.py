numeros = []
while True:
    numeros.append(int(input('Digite um valor para a lista: ')))
    continuar = str(input('Quer continuar? (s/n): ')).lower().strip()
    if continuar == 'n':
        break
print(f'Quantos valores foram digitados: {len(numeros)}')
numeros.sort(reverse=True)
print(f'A lista de valores na forma decrescente: {numeros}')
print(f'O valor 5 está na lista? {5 in numeros}')
