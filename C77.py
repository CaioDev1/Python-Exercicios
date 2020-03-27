palavras = 'Xarque', 'Fubas', 'Química', 'Brega', 'Sheldon'
for itens in palavras:
    print(f'A palavra {itens} tem as vogais: ', end=' ')
    for letra in itens:
        if letra in 'aeiou':
            print(letra, end=' ')
    print()
