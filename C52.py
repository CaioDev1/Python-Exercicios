num = int(input('Número: '))
divisores = 0
for contador in range(1, num + 1):
    if num % contador == 0:
        divisores += 1
if divisores == 2:
    print('O número é PRIMO')
else:
    print('O número NÃO é primo')
