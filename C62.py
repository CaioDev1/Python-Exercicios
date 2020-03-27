n1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
quantidade = int(input('Quer ver quantas sequencias? '))
while quantidade != 0:
    for cont2 in range(1, quantidade + 1):
        pa = n1 + (cont2 - 1) * r
        print(pa, end=' -> ')
    quantidade = int(input('Quer ver mais quantas termos seguintes? (0 finaliza): '))
    if quantidade != 0:
        n1 = pa
print('FINALIZADO')

