n1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
for contador in range(1, 11):
    pa = n1 + (contador - 1) * r
    print(pa, end=' -> ')
print('FINALIZADO')
