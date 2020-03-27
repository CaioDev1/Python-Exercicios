pessoas = []
pesado = 0
leve = 0
pesado_nome = []
leve_nome = []
while True:
    pessoas.append(str(input('Digite o nome: ')).lower().strip())
    pessoas.append(float(input('Digite o peso: ')))
    continuar = str(input('Quer continuar? (s/n): ').lower().strip())
    if continuar == 'n':
        break
quantidade = 0
print(f'Quantas pessoas foram cadastradas: ', end=' ')
for contador in range(0, len(pessoas)):
    if contador % 2 == 0:
        quantidade += 1
print(quantidade)
for contador in range(1, len(pessoas), 2):
    if contador == 1:
        pesado += pessoas[contador]
        leve += pessoas[contador]
    else:
        if pessoas[contador] > pesado:
            pesado = pessoas[contador]
            pesado_nome.append(pessoas[contador - 1])
        if pessoas[contador] < leve:
            leve = pessoas[contador]
            leve_nome.append(pessoas[contador - 1])
print(f'Listagens dos mais pesados: {pesado_nome}')
print(f'Listagens dos mais leves: {leve_nome}')




