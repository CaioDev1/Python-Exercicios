frase = str(input('Digite uma frase: ')).lower().strip()
print(f'Quantas vezes a letra A apareceu: {frase.count("a")}')
print(f'Em que posição ela aparece pela primeira vez: {frase.find("a")}')
print(f'Em que posição ela aparece pela última vez: {frase.rfind("a")}')

