from math import hypot, trunc
oposto = float(input('Cateto oposto: '))
adjacente = float(input('Cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print(f'O valor da hipotenusa é de: {trunc(hipotenusa)}')

