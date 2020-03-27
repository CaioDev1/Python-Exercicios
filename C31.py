km = int(input('Quantidade de kms da viagem: '))
if km >= 200:
    soma = km * 0.50
    print(f'O valor da passagem fica: {soma}')
else:
    soma = km * 0.45
    print(f'O valor da passagem fica: {soma}')
