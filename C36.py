valor = float(input('Valor da casa: '))
salario = float(input('Salário:'))
anos = int(input('Anos: '))
prestacao = valor / (anos * 12)
if prestacao > (salario * 30) / 100:
    print('Prestação excedeu 30% do salário, SITUAÇÃO NEGADA')
else:
    print('Empréstimo aprovado.')
