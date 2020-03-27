from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
if idade < 9:
    print('MIRIM')
elif 9 < idade < 14:
    print('INFANTIL')
elif 14 < idade < 19:
    print('JUNIOR')
elif 19 < idade < 20:
    print('SÊNIOR')
else:
    print('MASTER')
