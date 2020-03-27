n = int(input('Quantidade de sequências para Fibonacci: '))
cont = 0
x = 0
y = 1
z = x + y
while cont != n:
    print(x, end=' -> ')
    x = y
    y = z
    z = x + y
    cont += 1
print('FINALIZADO')
