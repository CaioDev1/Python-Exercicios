alunos = []
cont = 0
while True:
    alunos.append([])
    alunos[cont].append(str(input('Nome: ')))
    alunos[cont].append(float(input('Nota 1: ')))
    alunos[cont].append(float(input('Nota 2: ')))
    cont += 1
    continuar = str(input('Quer continuar? (s/n): ')).lower().strip()
    if continuar == 'n':
        break
print('No.  NOME         MÉDIA')
for contador in range(0, len(alunos)):
    print(f'{contador}  {alunos[contador][0]}       {(alunos[contador][1] + alunos[contador][2]) / 2}')
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 finaliza): '))
    if mostrar == 999:
        break
    else:
        print(f'Notas de {alunos[mostrar][0]} são: [{alunos[mostrar][1]}, {alunos[mostrar][2]}]')
