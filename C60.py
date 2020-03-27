num = int(input('Valor para o fatorial: '))
fat = num
contador = num - 1
print('5', end=' ')
while contador > 0:
    fat *= contador
    contador -= 1
    print(f'X {contador}', end=' ')
print(f'= {fat}')
