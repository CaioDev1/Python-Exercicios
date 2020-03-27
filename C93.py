jogador = {
    'nome': str(input('Nome do jogador: ')),
    'gols': []
}
soma = 0
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for contador in range(0, jogador['partidas']):
    jogador['gols'].append(int(input(f'Quantos gols na partida {contador + 1}: ')))
for itens in jogador['gols']:
    soma += itens
jogador['total'] = soma
print(jogador)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor: {value}')
print(f'O jogador jogou {jogador["partidas"]} partidas')
for contador in range(0, len(jogador.items())):
    print(f'Na partida {contador + 1} o jogador fez: {jogador["gols"][contador]} gols')
print(f'Foi um total de {soma} gols.')