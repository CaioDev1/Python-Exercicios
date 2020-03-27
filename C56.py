soma = 0
homem_velho = ''
homem_idade = 0
mulheres_20 = 0
for contador in range(0, 4):
    nome = str(input('Nome: ')).lower().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).lower().strip()
    soma += idade
    if contador == 0:
        if sexo == 'm':
            homem_idade = idade
    else:
        if sexo == 'm' and idade > homem_idade:
            homem_velho = nome
    if sexo == 'f' and idade < 20:
        mulheres_20 += 1
print(f'A média de idade é: {soma / 4}')
print(f'O nome do homem mais velho é: {homem_velho}')
print(f'O número de mulheres com menos de 20 anos é: {mulheres_20}')

