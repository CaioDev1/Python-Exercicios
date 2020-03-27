def maior(* numeros):
    maior_ = numeros[0]
    menor = numeros[0]
    for itens in numeros:
        if itens > maior:
            maior_ = itens
        if itens < menor:
            menor = itens
    print(f'O maior número é: {maior_}')
    print(f'O menor número é: {menor}')


maior(3, 5, 23, 53, 6, 1, 0)
