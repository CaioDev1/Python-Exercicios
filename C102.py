def fatorial(num, show=False):
    fat = num
    if show:
        print(f'{num} ', end='')
        for contador in range(num - 1, 0, -1):
            print(f'X {contador}', end=' ')
            fat *= contador
        print(f'= {fat}')
    else:
        for contador in range(num - 1, 0, -1):
            fat *= contador
        print(fat)


fatorial(5)
