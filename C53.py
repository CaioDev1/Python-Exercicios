frase = str(input('Digite uma frase: ')).lower().strip().split()
frase_sem_espaco = ''.join(frase)
frase_contrario = frase_sem_espaco[::-1]
if frase_sem_espaco == frase_contrario:
    print('É UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')

#alternativo

frr = ''
for contador in range(len(frase_sem_espaco) - 1, -1, -1):
    frr += frase_sem_espaco[contador]
print(frr)
