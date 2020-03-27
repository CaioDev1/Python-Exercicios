from datetime import date
ano_atual = date.today().year
pessoa = {
    'nome': str(input('Nome: ')).strip(),
    'nascimento': int(input('Ano de nascimento: ')),
    'carteira': int(input('Carteira de trabalho: '))
}
pessoa['idade'] = ano_atual - pessoa['nascimento']
if pessoa['carteira'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = (pessoa['contratacao_ano'] - pessoa['nascimento']) + 35
for key, value in pessoa.items():
    print(f'{key} tem o valor: {value}')