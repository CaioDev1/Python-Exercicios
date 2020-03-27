produtos = 'Frango', 15.00, 'Charque', 3.56, 'Fubas', 6.64, 'Inhame', 5.00
for contador in range(0, len(produtos)):
    if contador % 2 == 0:
        print(f'{produtos[contador]} \t\t\t', end='')
    else:
        print(produtos[contador])
