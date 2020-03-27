from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
if idade < 18:
    print(f'Ainda vai se alistar, faltam {18 - idade} até lá')
elif idade == 18:
    print('Está na hora de se alistar')
else:
    print(f'Passou do tempo de se alistar, você está atrasado {idade - 18} anos')
