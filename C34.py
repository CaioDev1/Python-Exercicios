salario = float(input('Salário: '))
if salario > 1250:
    salario = salario + (salario * 10) / 100
    print(f'O novo salário é: {salario}')
else:
    salario = salario + (salario * 15) / 100
    print(f'O novo salário é: {salario}')
