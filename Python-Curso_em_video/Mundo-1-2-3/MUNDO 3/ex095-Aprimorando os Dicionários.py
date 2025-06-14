"""Aprimore o desafio 93 para que ele funcione com vários
jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador."""
time = []
print(f'{'-=' * 15}{'\nAPROVEITAMENTO DO CAMPEONATO'}\n{'-=' * 15}')
s = 0
while True:
    campeonato = {'nome': str(input('Nome do Jogador: ')).title(), 'gols': []}
    campeonato['partidas'] = int(input(f'Quantas partidas {campeonato['nome']} jogou? '))
    for p in range(1, campeonato['partidas'] + 1):
        ponto = int(input(f'Quantos gols na partida {p}? '))
        campeonato['gols'].append(ponto)
    campeonato['total'] = sum(campeonato['gols'])
    time.append(campeonato.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-=' * 15)
    if continuar == 'N':
        break

#CABEÇALHO TABELA
print(f'{'-' * 40}\n{"COD":^5}'
      f'{"NOME":^10}'
      f'{"GOLS":^15}'
      f'{"TOTAL":^10}\n{'-' * 40}')

#TABELA
for k, v in enumerate(time):
    if v in time :
        gols_formatados = str(v["gols"])
        print(f'{k+1:^5}'
              f'{v["nome"]:^10}'
              f'{gols_formatados:^15}'
              f'{v["total"]:^10}\n')

#DETALHES POR JOGADOR
while True:
    detalhes = int(input(f'{'-' * 40}\n'
                         f'Mostrar dados de qual jogador?[999 para parar] '))
    if detalhes == 999:
        print('>>>VOLTE SEMPRE<<<')
        break
    elif detalhes < 1 or detalhes > len (time):
        print(f'ERRO! Não existe jogador com código {detalhes}! TENTE NOVAMENTE...')
    else:
        jogador = time[detalhes-1]
        print(f'--LEVANTAMENTO DO JOGADOR {jogador['nome']}:')
        for i, g in enumerate(jogador['gols']):
            print(f'    => Na partida {i+1}, fez {g} gols.')
