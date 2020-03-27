total = 0
mais1000 = 0
barato_preco = 0
barato_nome = ''
while True:
    produto = str(input('Nome do produto: ')).lower().strip()
    preco = float(input('Preço do produto: '))
    if total == 0:
        barato_preco = preco
        barato_nome = produto
    else:
        if preco > 1000:
            mais1000 += 1
        if preco < barato_preco:
            barato_preco = preco
            barato_nome = produto
        total += preco
        continuar = str(input('Continuar? (s/n): ')).lower().strip()
        if continuar == 'n':
            break
print(f'O total do valor dos produtos: {total}')
print(f'A quantidade de produtos com mais de R$ 1000: {mais1000}')
print(f'O nome do produto mais barato é: {barato_nome}')
