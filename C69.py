p_18mais = 0
homens = 0
mulheresmenos20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (m/f): ')).lower().strip()
    if idade > 18:
        p_18mais += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheresmenos20 += 1
    continuar = str(input('Continuar? (s/n): ')).lower().strip()
    if continuar == 'n':
        break
print(f'O número de pessoas com mais de 18: {p_18mais}')
print(f'O número de homens: {homens}')
print(f'O número de mulheres com menos de 20 anos: {mulheresmenos20}')
