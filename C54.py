from datetime import date
maiores = 0
menores = 0
ano_atual = date.today().year
for contador in range(0, 7):
    ano_nasc = int(input('Ano de nascimento: '))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f'A quantidade de maiores são: {maiores}')
print(f'A quantidade de menores são: {menores}')
