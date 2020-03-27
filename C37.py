
num = int(input('Número: '))
print('1 - BINÁRIO \n 2 - OCTAL \n 3 - HEXADECIMAL')
escolha = int(input('Opção: '))
if escolha == 1:
    print(bin(num))
elif escolha == 2:
    print(oct(num))
else:
    print(hex(num))
