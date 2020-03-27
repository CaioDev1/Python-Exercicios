pessoa = {
        'nome': '',
        'idade': 0,
        'sexo': ''
    }
pessoas = []
quantidade = 0
media = 0
soma = 0
mulheres = []
acima_media_idade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = str(input('Sexo (m/f): ')).lower().strip()
    pessoas.append(pessoa.copy())
    quantidade += 1
    soma += pessoa['idade']
    if pessoa['sexo'] == 'f':
        mulheres.append(pessoa['sexo'])
    continuar = str(input('Continuar? (s/n): ')).lower().strip()
    if continuar == 'n':
        break
media = soma / len(pessoas)
print(pessoas)
print(f'Quantidade de pessoas cadastradas: {quantidade}')
print(f'Média de idade do grupo: {media}')
print(f'Lista com nome das mulheres: {mulheres}')
print('Lista com pessoas com idade acima da média: ')
for contador in range(0, len(pessoas)):
    if pessoas[contador]['idade'] > media:
        print(f'{pessoas[contador]["nome"]}')

