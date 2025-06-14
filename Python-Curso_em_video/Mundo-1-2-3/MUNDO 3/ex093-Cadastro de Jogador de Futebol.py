"""Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador e quantas partidas ele
jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos
durante o campeonato."""
print(f'{'-=' * 15}{'\nAPROVEITAMENTO DO CAMPEONATO'}\n{'-=' * 15}')
campeonato = {'nome': str(input('Nome: ')).title(), 'gols': []}
partidas = int(input(f'Quantas partidas {campeonato["nome"]} jogou? '))
for p in range (1, partidas+1):
    ponto = int(input(f'Quantos gols na partida {p}? '))
    campeonato["gols"].append(ponto)
campeonato["total"] = sum(campeonato["gols"])
print(f'{'-=' * 20}\n{campeonato}\n{'-=' * 20}')
for k, v in campeonato.items():
   print(f'O campo {k} tem o valor {v}.')
print(f'{'-=' * 20}\n'
      f'O jogador {campeonato["nome"]} jogou {partidas} partidas:')
for i, p in enumerate(campeonato['gols']):
    print(f'    => Na partida {i+1}, fez {p} gols.')
print(f'Foi um total de {campeonato["total"]} gols.')
