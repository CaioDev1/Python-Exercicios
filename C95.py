jogadores = []
soma = 0
while True:
    jogador = {
        'nome': '',
        'gols': []
    }
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for contador in range(0, jogador['partidas']):
        gol = int(input(f'Quantas gols na partida {contador + 1}: '))
        jogador['gols'].append(gol)
        soma += gol
    jogador['total'] = soma
    jogadores.append(jogador.copy())
    escolha = str(input('Quer continuar (s/n): ')).lower().strip()
    if escolha == 'n':
        break
print('Cod.   Nome      Gols      Total')
for contador in range(0, len(jogadores)):
    print(f'{contador}  {jogadores[contador]["nome"]}         {jogadores[contador]["gols"]}    {jogadores[contador]["total"]}')
while True:
    continuar = int(input('Mostrar dados de qual jogador (999) finaliza: '))
    if continuar != 999:
        if continuar >= len(jogadores):
            print(f'ERRO, NÃO EXISTE JOGADOR COM NÚMERO {continuar}')
        else:
            print(f'LEVANTAMENTO DO JOGADOR: {jogadores[continuar]["nome"]}')
            for contador in range(0, len(jogadores[continuar]['gols'])):
                print(f'No jogo {contador} fez {jogadores[continuar]["gols"][contador]}')
    else:
        break
print('FINALIZADO')
