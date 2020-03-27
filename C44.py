preco = float(input('Valor do produto: '))
print('1 - A vista dinheiro/cheque \n  2 - A vista cartão \n 3 - 2x cartão \n 3x ou mais cartão')
opcao = int(input('Opção: '))
if opcao == 1:
    print(f'O preço do produto fica: {preco - (preco * 10) / 100}')
elif opcao == 2:
    print(f'O preço do produto fica: {preco - (preco * 5) / 100}')
elif opcao == 3:
    print(f'O preço do produto fica: {preco}')
else:
    print(f'O preço do produto fica: {preco + (preco * 20) / 100}')
