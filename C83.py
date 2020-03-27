expressao = str(input('Digite a expressão: '))
expressao_array = []
parE = 0
parD = 0
for letras in expressao:
    expressao_array.append(letras)
for itens in expressao_array:
    if itens == '(':
        parE += 1
    if itens == ')':
        parD += 1
if parD == parE:
    print(f'A expressão: {expressao} É VÁLIDA')
else:
    print(f'A expressão: {expressao} NÃO É VÁLIDA')
