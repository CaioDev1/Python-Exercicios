from datetime import date


def voto(nasc, atual):
    idade = atual - nasc
    if idade < 16:
        return 'NEGADO'
    elif 16 < idade < 18 or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
print(f'Com {ano_atual - ano_nascimento} a situação é: {voto(ano_nascimento)}')
