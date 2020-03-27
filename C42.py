l1 = int(input('lado 1: '))
l2 = int(input('lado 2: '))
l3 = int(input('lado 3: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 and l1 == l3:
        print('É UM TRIÂNGULO EQUILÁTERO')
    elif l1 == l2 or l1 == l3:
        print('É UM TRIÂNGULO ISÓSCELES')
    else:
        print('É UM TRIÂNGULO ESCALENO')
else:
    print('NÃO FORMA UM TRIÂNGULO')