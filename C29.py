vel = int(input('Velocidade do carro: '))
if vel > 80:
    print('MULTADO')
    soma = vel * 7
    print(f'Valor da multa: {soma}')
else:
    print('Tudo ok')
