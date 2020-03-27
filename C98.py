def contador(i, f, p=1):
    if i <= f:
        for c in range(i, f + 1, p):
            print(c, end=' -> ')
        print('FINALIZADO')
    else:
        for c in range(i, f - 2, -p):
            print(c, end=' -> ')
        print('FINALIZADO')


contador(1, 10)
contador(10, 1, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
