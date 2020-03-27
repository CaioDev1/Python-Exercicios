numeros = []


def nalista(num):
    if num in numeros:
        return True
    else:
        return False


while True:
    n = int(input('Adicione um valor a lista: '))
    if not nalista(n):
        numeros.append(n)
    else:
        print(f'Número {n} já na lista.')
    continuar = str(input('Continuar? (s/n): ')).lower().strip()
    if continuar == 'n':
        break
print(numeros)
print('FINALIZADO')
