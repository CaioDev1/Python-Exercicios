nome = str(input('Digite o nome: ')).strip()
print(f'Nome com letras maiúsculas: {nome.upper()}')
print(f'Nome com letras minúsculas: {nome.lower()}')
print(f'Quantas letras ao todo: {len(nome) - nome.count(" ")}')
print(f'O primeiro nome tem: {nome.find(" ")} letras')

