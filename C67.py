while True:
    tabuada = int(input('Valor para a tabuada (n° negativo finaliza): '))
    if tabuada < 0:
        break
    else:
        for contador in range(1, 11):
            print(f'{tabuada} X {contador} = {tabuada * contador}')
print('FINALIZADO')
