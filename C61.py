n1 = int(input('Primeiro valor da PA: '))
r = int(input('Razão da PA: '))
cont = 1
while cont < 11:
    pa = n1 + (cont - 1) * r
    print(pa, end=' -> ')
    cont += 1
print('FINALIZADO')
