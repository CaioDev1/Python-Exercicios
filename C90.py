aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media']= float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 6:
    aluno['situação'] = 'REPROVADO'
else:
    aluno['situação'] = 'APROVADO'
print(f'Nome é igual a: {aluno["nome"]}')
print(f'Média é igual a: {aluno["media"]}')
print(f'Situação é igual a: {aluno["situação"]}')

